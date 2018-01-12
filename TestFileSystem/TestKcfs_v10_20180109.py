#!/usr/bin/env python
# https://github.com/billziss-gh/secfs.test/blob/master/fsrand/fsrand.py

# Copyright (c) 2015, Bill Zissimopoulos. All rights reserved.
#
# Redistribution  and use  in source  and  binary forms,  with or  without
# modification, are  permitted provided that the  following conditions are
# met:
#
# 1.  Redistributions  of source  code  must  retain the  above  copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions  in binary  form must  reproduce the  above copyright
# notice,  this list  of conditions  and the  following disclaimer  in the
# documentation and/or other materials provided with the distribution.
#
# 3.  Neither the  name  of the  copyright  holder nor  the  names of  its
# contributors may  be used  to endorse or  promote products  derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY  THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND  ANY EXPRESS OR  IMPLIED WARRANTIES, INCLUDING, BUT  NOT LIMITED
# TO,  THE  IMPLIED  WARRANTIES  OF  MERCHANTABILITY  AND  FITNESS  FOR  A
# PARTICULAR  PURPOSE ARE  DISCLAIMED.  IN NO  EVENT  SHALL THE  COPYRIGHT
# HOLDER OR CONTRIBUTORS  BE LIABLE FOR ANY  DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL,  EXEMPLARY,  OR  CONSEQUENTIAL   DAMAGES  (INCLUDING,  BUT  NOT
# LIMITED TO,  PROCUREMENT OF SUBSTITUTE  GOODS OR SERVICES; LOSS  OF USE,
# DATA, OR  PROFITS; OR BUSINESS  INTERRUPTION) HOWEVER CAUSED AND  ON ANY
# THEORY  OF LIABILITY,  WHETHER IN  CONTRACT, STRICT  LIABILITY, OR  TORT
# (INCLUDING NEGLIGENCE  OR OTHERWISE) ARISING IN  ANY WAY OUT OF  THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os, random
import sys
import glob
import logging
import logging.handlers
import shutil
import time
import subprocess

class Devnull(object):
    def write(self, *args):
        pass
devnull = Devnull()

# https://pymotw.com/2/logging/
LOG_FILENAME1 = 'kcfsTestScript-init.log'

# Set up a specific logger with our desired output level
my_base_logger = logging.getLogger('MyBaseLogger')

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME1,
                                               maxBytes=100000000,
                                               backupCount=50,
                                               )
my_base_logger.addHandler(handler)
my_base_logger.setLevel(logging.DEBUG)

# --------------------------------------------------------------------------
# Main Class
# --------------------------------------------------------------------------
class FsRandomizer(object):

    def __init__(self, basepath, kcfspath, count, maxoffset, loglevel, dirdepth, logfile, diffcheck, seed):
        self.stdout = devnull
        self.stderr = devnull
        self.maxlen = 128*1024
        self.maxofs = maxoffset
        self.kcfspath = os.path.realpath(kcfspath)
        self.basepath = os.path.realpath(basepath)
        self.count = count
        self.dirdepth = str(dirdepth)
        self.random = random.Random(seed)
        self.operation = None
        self.diffcheck = diffcheck
        loglevel = str(loglevel)
        # https://pymotw.com/2/logging/
        LOG_FILENAME2 = str(logfile)

        # Set up a specific logger with our desired output level
        self.my_logger = logging.getLogger('MyLogger')

        # Add the log message handler to the logger
        handler = logging.handlers.RotatingFileHandler(LOG_FILENAME2,
                                                       maxBytes=100000000,
                                                       backupCount=50,
                                                       )
        self.my_logger.addHandler(handler)
        if loglevel.lower() == "debug":
            self.my_logger.setLevel(logging.DEBUG)
        elif loglevel.lower() == "info":
            self.my_logger.setLevel(logging.INFO)
        elif loglevel.lower() == "warning":
            self.my_logger.setLevel(logging.WARNING)
        elif loglevel.lower() == "error":
            self.my_logger.setLevel(logging.ERROR)
        elif loglevel.lower() == "critical":
            self.my_logger.setLevel(logging.CRITICAL)
        else:
            self.my_logger.setLevel(logging.INFO)


    def __listdir_nohidden(self, path):
        for f in os.listdir(path):
            if not f.startswith('.'):
                yield f

    def __listfiles_nohidden(self, path):
        fullFilesList = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        filesList = [f for f in fullFilesList if not f.startswith('.')]
        return filesList

    # --------------------------------------------------------------------------
    # __getdir_recurse
    # This gets a deeper directory path
    # --------------------------------------------------------------------------
    def __getdir_recurse(self, path):
        try:
            n = self.random.choice(list(self.__listdir_nohidden(path)))
        except Exception as e:
            #self.my_logger.error("%s ERROR Exception in __getdir_recurse=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), e))
            return path
        p = os.path.join(path, n)
        if os.path.isdir(p):
            return self.__getdir_recurse(p)
        else:
            return path

    # --------------------------------------------------------------------------
    # __getdir
    # From the deeper directory path, pick a random intermediate path and use that
    # --------------------------------------------------------------------------
    def __getdir(self, basepath, kcfspath):
        # This is to avoid race between other threads
        newpath = self.__getdir_recurse(kcfspath)
        newpath = basepath + newpath.replace(kcfspath, '')
        self.my_logger.debug("%s DEBUG Deeppath=%s; basepath=%s; kcfspath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), newpath, basepath, kcfspath))
        if self.dirdepth.lower() == "deep":
            return newpath
        else:
            p = newpath.replace(basepath, '')
            parts = p.split(os.sep)
            parts = parts[0:self.random.randint(1, len(parts))]
            finalpath = os.path.join(basepath, *parts)
            self.my_logger.debug("%s DEBUG Random path between basepath and deep path=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), finalpath))
            return finalpath

    def __getsubpath(self, path):
        try:
            n = self.random.choice(list(self.__listdir_nohidden(path)))
            self.my_logger.debug("%s DEBUG Random file/dir in path %s: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), path, n))
        except Exception as e:
            self.my_logger.error("%s ERROR Exception in __getsubpath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), e))
            return path
        return os.path.join(path, n)

    def __getsubfilepath(self, path):
        try:
            n = self.random.choice(list(self.__listfiles_nohidden(path)))
            self.my_logger.debug("%s DEBUG Random file in path %s: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), path, n))
        except Exception as e:
            #self.my_logger.error("%s ERROR Exception in __getsubfilepath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), e))
            return path
        return os.path.join(path, n)

    def __newname(self):
        l = self.random.randint(1, 16)
        n = [self.random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in xrange(l)]
        return "".join(n)

    def __newsubpath(self, path):
        while True:
            p = os.path.join(path, self.__newname())
            if not os.path.exists(p):
                return p

    def __newmode(self, mode):
        return mode | self.random.randint(0, 077)

    def __random_write(self, file):
        o = self.random.randint(0, self.maxofs)
        l = self.random.randint(0, self.maxlen)
        b = [self.random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in xrange(l)]
        file.seek(o)
        file.write("".join(b))
        self.my_logger.info("%s INFO %s: __random_write file=%s; offset=%d; numBytes=%d" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, file.name, o, len(b)))
        return o, b

    def __fixed_write(self, file, o, b):
        file.seek(o)
        file.write("".join(b))
        self.my_logger.info("%s INFO %s: __fixed_write file=%s; offset=%d; numBytes=%d" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, file.name, o, len(b)))

    def __random_read(self, file):
        file.seek(0, 2)
        eof = file.tell()
        offset = random.randint(0, eof)
        numBytes = random.randint(0, eof - offset)
        file.seek(offset)
        data = file.read(numBytes)
        self.my_logger.info("%s INFO %s: __random_read file=%s; offset=%d; numBytes=%d" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, file.name, offset, numBytes))
        return offset, numBytes

    def __fixed_read(self, file, o, b):
        file.seek(o)
        data = file.read(b);
        self.my_logger.info("%s INFO %s: __fixed_read file=%s; offset=%d, numBytes=%d" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, file.name, o, b))

    def __create(self, path, israndom, offset=None, data=None):
        with open(path, "wb") as f:
            if israndom:
                return self.__random_write(f)
            else:
                return self.__fixed_write(f, offset, data)

    def __update(self, path, israndom, offset=None, data=None):
        if not os.path.exists(path):
            self.my_logger.error("%s ERROR %s: __update path does not exist: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, path))
            return None, None
        with open(path, "r+b") as f:
            if israndom:
                return self.__random_write(f)
            else:
                return self.__fixed_write(f, offset, data)

    def __read(self, path, israndom, offset=None, numBytes=None):
        if not os.path.exists(path):
            self.my_logger.error("%s ERROR %s: __read path does not exist: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, path))
            return None, None
        with open(path, "r+b") as f:
            if israndom:
                return self.__random_read(f)
            else:
                return self.__fixed_read(f, offset, numBytes)

    # --------------------------------------------------------------------------
    # __randomize
    # This function takes care of performing an operation at random
    # It does Create/Read/Write/Delete
    # --------------------------------------------------------------------------
    def __randomize(self, itr):
        #op = self.random.choice("CRWD")
        # Ignore delete for now
        op = self.random.choice("CRW")
        self.my_logger.info("\n%s INFO Iteration: %d; Operation: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), int(itr), op))
        if op == "C":
            self.operation = "CREATE"
            basepath = self.__newsubpath(self.__getdir(self.basepath, self.kcfspath))
            newPath = basepath.replace(self.basepath, '')
            kcfspath = self.kcfspath + newPath
            self.my_logger.debug("%s DEBUG CREATE basePath=%s; kcfsPath=%s; newPath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath, kcfspath, newPath))
            if self.random.randint(0, 1):
                offset, data = self.__create(basepath, True)
                if offset is None or data is None:
                    return
                self.my_logger.debug("%s DEBUG CREATE file basePath=%s; kcfsPath=%s; offset=%d" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath, kcfspath, offset))
                self.__create(kcfspath, False, offset, data)
            else:
                self.my_logger.info("%s INFO CREATE directory basePath=%s; kcfsPath=%s; newPath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath, kcfspath, newPath))
                os.mkdir(basepath)
                os.mkdir(kcfspath)
        elif op == "D":
            self.operation = "DELETE"
            basepath = self.__getsubpath(self.__getdir(self.basepath, self.kcfspath))
            newPath = basepath.replace(self.basepath, '')
            kcfspath = self.kcfspath + newPath
            if os.path.realpath(basepath) == self.basepath:
                self.my_logger.info("%s INFO Skipping DELETE operation on parent directory=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.basepath))
                return
            self.my_logger.debug("%s DEBUG REMOVE basepath=%s kcfspath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath, kcfspath))
            if not os.path.isdir(basepath):
                os.unlink(basepath)
                self.my_logger.info("%s INFO %s: fileDelete file=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, basepath))
                os.unlink(kcfspath)
                self.my_logger.info("%s INFO %s: fileDelete file=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, kcfspath))
            else:
                try:
                    os.rmdir(basepath)
                    self.my_logger.info("%s INFO %s: dirDelete dir=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, basepath))
                    os.rmdir(kcfspath)
                    self.my_logger.info("%s INFO %s: dirDelete dir=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.operation, kcfspath))
                except Exception as e:
                    self.my_logger.error("%s ERROR Exception in __randomize delete=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), e))
                    pass
        elif op == "W":
            self.operation = "WRITE"
            basepath = self.__getsubfilepath(self.__getdir(self.basepath, self.kcfspath))
            newPath = basepath.replace(self.basepath, '')
            kcfspath = self.kcfspath + newPath
            # Ignore SetAttr for now
            if os.path.realpath(basepath) == self.basepath:
                self.my_logger.info("%s INFO Skipping WRITE operation on parent directory=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.basepath))
                return
            self.my_logger.debug("%s DEBUG UPDATE basepath=%s; kcfspath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath, kcfspath))
            if os.path.isdir(basepath):
                self.my_logger.info("%s INFO Skipping WRITE operation on dir=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath))
                return
            offset, data = self.__update(basepath, True)
            if offset is None or data is None:
                return;
            self.__update(kcfspath, False, offset, data)
            self.my_logger.debug("%s DEBUG UPDATE offset=%d" % (time.strftime("%Y-%m-%d %H:%M:%S"), offset))
        elif op == "R":
            self.operation = "READ"
            basepath = self.__getsubfilepath(self.__getdir(self.basepath, self.kcfspath))
            newPath = basepath.replace(self.basepath, '')
            kcfspath = self.kcfspath + newPath
            if os.path.realpath(basepath) == self.basepath:
                self.my_logger.info("%s INFO Skipping READ operation on parent directory=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.basepath))
                return
            if os.path.isdir(basepath):
                self.my_logger.info("%s INFO Skipping READ operation on dir=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath))
                return
            self.my_logger.debug("%s DEBUG READ basepath=%s; kcfspath=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), basepath, kcfspath))
            offset, numBytes = self.__read(basepath, True)
            if offset is None or numBytes is None:
                return;
            self.__read(kcfspath, False, offset, numBytes)

    # --------------------------------------------------------------------------
    # __checkDirectories
    # This function performs a diff between two directories
    # At any point if the diff does not match we can stop running the script
    # --------------------------------------------------------------------------
    def __checkDirectories(self, itr, basepath, kcfspath):
        if itr % self.diffcheck == 0:
            bashCommand = "diff -x .* -r " + self.basepath + " " + self.kcfspath
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if output:
                self.my_logger.error("%s ERROR Iteration=%d; Diff mismatch=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), itr, output))
            else:
                self.my_logger.debug("%s DEBUG Iteration=%d; Diff matches" % (time.strftime("%Y-%m-%d %H:%M:%S"), itr))
            return output

    # --------------------------------------------------------------------------
    # randomizeOp
    # This is the base function that performs the iterations
    # --------------------------------------------------------------------------
    def randomizeOp(self):
        # Argument to perform infinite runs
        if self.count.lower() == "inf":
            itr = 0
            while True:
                output = self.__checkDirectories(itr, self.basepath, self.kcfspath)
                if output:
                    break
                self.__randomize(itr)
                itr = itr + 1
        elif not self.count.isdigit():
            # Incase an invalid argument is passed, perform run for 100 iterations
            self.count = 100
        for i in xrange(int(self.count)):
            output = self.__checkDirectories(i, self.basepath, self.kcfspath)
            if output:
                break
            self.__randomize(i)
        # Do diff check after finishing the iterations
        output = self.__checkDirectories(0, self.basepath, self.kcfspath)

# --------------------------------------------------------------------------
# This is the entry point of the script. Parse command line arguments and
# start the iterations
# --------------------------------------------------------------------------
if "__main__" == __name__:
    import argparse, sys, time

    def info(s):
        print "%s: %s" % (os.path.basename(sys.argv[0]), s)

    def warn(s):
        print >> sys.stderr, "%s: %s" % (os.path.basename(sys.argv[0]), s)

    def fail(s, exitcode = 1):
        warn(s)
        sys.exit(exitcode)

    def main():
        p = argparse.ArgumentParser()
        p.add_argument("-c", "--count", default="100")
        p.add_argument("-o", "--maxoffset", type=int, default=10*1024*1024)
        p.add_argument("-l", "--loglevel", default=info)
        p.add_argument("-s", "--seed", type=int, default=0)
        p.add_argument("-d", "--dirdepth", default="deep")
        p.add_argument("-f", "--logfile", default="kcfsTestScript.log")
        p.add_argument("-i", "--diffcheck", type=int, default=100)
        p.add_argument("basepath")
        p.add_argument("kcfspath")
        args = p.parse_args(sys.argv[1:])
        if args.seed == 0:
            args.seed = int(time.time())
        if not os.path.isdir(args.basepath):
            fail("Base path must exist and be a directory")
        os.umask(0)
        fsrand = FsRandomizer(args.basepath, args.kcfspath, args.count, args.maxoffset, args.loglevel, args.dirdepth, args.logfile, args.diffcheck, args.seed)
        fsrand.stdout = sys.stdout
        fsrand.stderr = sys.stderr
        my_base_logger.info("\n\n%s INFO TestKcfs: basePath=%s; kcfsPath=%s; count=%s; maxoffset=%d, loglevel=%s; dirdepth=%s; logfile=%s; diffcheck=%d; seed=%s" %
                            (time.strftime("%Y-%m-%d %H:%M:%S"), args.basepath, args.kcfspath, args.count, args.maxoffset, args.loglevel, args.dirdepth, args.logfile, args.diffcheck, args.seed))
        fsrand.randomizeOp()

    def __entry():
        try:
            main()
        except EnvironmentError, e:
            my_base_logger.error("%s ERROR EnvironmentError in __entry=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), e))
            fail(e)
        except KeyboardInterrupt as e:
            my_base_logger.error("%s ERROR KeyboardInterrupt in __entry=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), e))
            fail("interrupted", 130)
        except Exception as e:
            my_base_logger.error("%s ERROR Exception in __entry=%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), e))

    __entry()

