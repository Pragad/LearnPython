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

# https://pymotw.com/2/logging/
LOG_FILENAME = 'kcfsTestScript.log'

LEVELS = { 'debug':logging.DEBUG,
           'info':logging.INFO,
           'warning':logging.WARNING,
           'error':logging.ERROR,
           'critical':logging.CRITICAL,
         }
# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')

# Set log level from user
#if len(sys.argv) > 1:
#    level_name = sys.argv[1]
#    level = LEVELS.get(level_name, logging.NOTSET)
my_logger.setLevel(logging.INFO)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                               maxBytes=999999,
                                               backupCount=5,
                                               )
my_logger.addHandler(handler)

class Devnull(object):
    def write(self, *args):
        pass
devnull = Devnull()

class FsRandomizer(object):

    def __init__(self, basepath, kcfspath, count, seed):
        self.stdout = devnull
        self.stderr = devnull
        self.verbose = 0
        self.maxofs = 1*1024*1024
        self.maxlen = 128*1024
        self.kcfspath = os.path.realpath(kcfspath)
        self.basepath = os.path.realpath(basepath)
        self.count = count
        self.random = random.Random(seed)
        self.dictionary = None
        self.operation = None

    def __getdir_recurse(self, path):
        try:
            n = self.random.choice(os.listdir(path))
        except:
            return path
        p = os.path.join(path, n)
        if os.path.isdir(p):
            return self.__getdir_recurse(p)
        else:
            return path

    def __getdir(self, path):
        p = self.__getdir_recurse(path)
        parts = p[len(p):].split(os.sep)
        parts = parts[0:self.random.randint(1, len(parts))]
        return os.path.join(path, *parts)

    def __getsubpath(self, path):
        try:
            n = self.random.choice(os.listdir(path))
        except:
            return path
        return os.path.join(path, n)

    def __newname(self):
        if self.dictionary:
            return self.random.choice(self.dictionary)
        else:
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
        my_logger.info("%s: __random_write file=%s; offset=%d" % (self.operation, file.name, o))
        return o, b

    def __fixed_write(self, file, o, b):
        file.seek(o)
        file.write("".join(b))
        my_logger.info("%s: __fixed_write file=%s; offset=%d" % (self.operation, file.name, o))

    def __random_read(self, file):
        file.seek(0, 2)
        eof = file.tell()
        offset = random.randint(0, eof)
        numBytes = random.randint(0, eof - offset)
        file.seek(offset)
        data = file.read(numBytes)
        my_logger.info("%s: __random_read file=%s; offset=%d" % (self.operation, file.name, offset))
        return offset, numBytes

    def __fixed_read(self, file, o, b):
        file.seek(o)
        data = file.read(b);
        my_logger.info("%s: __fixed_read file=%s; offset=%d" % (self.operation, file.name, o))

    def __create(self, path, israndom, offset=None, data=None):
        assert not os.path.exists(path)
        with open(path, "wb") as f:
            if israndom:
                return self.__random_write(f)
            else:
                return self.__fixed_write(f, offset, data)

    def __update(self, path, israndom, offset=None, data=None):
        assert os.path.exists(path)
        with open(path, "r+b") as f:
            if israndom:
                return self.__random_write(f)
            else:
                return self.__fixed_write(f, offset, data)

    def __read(self, path, israndom, offset=None, numBytes=None):
        assert os.path.exists(path)
        with open(path, "r+b") as f:
            if israndom:
                return self.__random_read(f)
            else:
                return self.__fixed_read(f, offset, numBytes)

    def randomize(self):
        for i in xrange(self.count):
            op = self.random.choice("CRWD")
            my_logger.info("\nIteration: %d; Operation: %s" % (i, op))
            if op == "C":
                self.operation = "CREATE"
                basepath = self.__newsubpath(self.__getdir(self.basepath))
                newPath = basepath.replace(self.basepath, '')
                kcfspath = self.kcfspath + newPath
                if self.verbose:
                    my_logger.debug("CREATE basePath=%s kcfsPath=%s newPath=%s" % (basepath, kcfspath, newPath))
                if self.random.randint(0, 1):
                    offset, data = self.__create(basepath, True)
                    self.__create(kcfspath, False, offset, data)
                else:
                    os.mkdir(basepath)
                    os.mkdir(kcfspath)
            elif op == "D":
                self.operation = "DELETE"
                basepath = self.__getsubpath(self.__getdir(self.basepath))
                newPath = basepath.replace(self.basepath, '')
                kcfspath = self.kcfspath + newPath
                if os.path.realpath(basepath) == self.basepath:
                    continue
                if self.verbose:
                    my_logger.debug("REMOVE basepath=%s kcfspath=%s" % (basepath, kcfspath))
                if not os.path.isdir(basepath):
                    shutil.copyfile(basepath, basepath + ".old")
                    os.unlink(basepath)
                    my_logger.info("%s: fileDelete file=%s" % (self.operation, basepath))
                    shutil.copyfile(kcfspath, kcfspath + ".old")
                    os.unlink(kcfspath)
                    my_logger.info("%s: fileDelete file=%s" % (self.operation, kcfspath))
                else:
                    try:
                        shutil.copytree(basepath, basepath + ".old")
                        os.rmdir(basepath)
                        my_logger.info("%s: dirDelete dir=%s" % (self.operation, basepath))
                        shutil.copytree(kcfspath, kcfspath + ".old")
                        os.rmdir(kcfspath)
                        my_logger.info("%s: dirDelete dir=%s" % (self.operation, kcfspath))
                    except:
                        pass
            elif op == "W":
                self.operation = "WRITE"
                basepath = self.__getsubpath(self.__getdir(self.basepath))
                newPath = basepath.replace(self.basepath, '')
                kcfspath = self.kcfspath + newPath
                # Ignore SetAttr for now
                if os.path.realpath(basepath) == self.basepath:
                    continue
                if self.verbose:
                    my_logger.debug("UPDATE basepath=%s kcfspath=%s" % (basepath, kcfspath))
                if not os.path.isdir(basepath):
                    offset, data = self.__update(basepath, True)
                    self.__update(kcfspath, False, offset, data)
                    my_logger.debug("UPDATE offset=%d" % offset)
            elif op == "R":
                self.operation = "READ"
                basepath = self.__getsubpath(self.__getdir(self.basepath))
                newPath = basepath.replace(self.basepath, '')
                kcfspath = self.kcfspath + newPath
                if os.path.realpath(basepath) == self.basepath:
                    continue
                if os.path.isdir(basepath):
                    continue
                if self.verbose:
                    my_logger.debug("READ basepath=%s kcfspath=%s" % (basepath, kcfspath))
                    offset, numBytes = self.__read(basepath, True)
                    self.__read(kcfspath, False, offset, numBytes)

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
        p.add_argument("-v", "--verbose", action="count", default=0)
        p.add_argument("-c", "--count", type=int, default=100)
        p.add_argument("-s", "--seed", type=int, default=0)
        p.add_argument("-d", "--dictionary")
        p.add_argument("basepath")
        p.add_argument("kcfspath")
        args = p.parse_args(sys.argv[1:])
        if args.seed == 0:
            args.seed = int(time.time())
        if not os.path.isdir(args.basepath):
            fail("base path must exist and be a directory")
        if args.dictionary:
            with open(args.dictionary) as f:
                args.dictionary = [l.strip() for l in f]
        os.umask(0)
        fsrand = FsRandomizer(args.basepath, args.kcfspath, args.count, args.seed)
        fsrand.dictionary = args.dictionary
        fsrand.stdout = sys.stdout
        fsrand.stderr = sys.stderr
        fsrand.verbose = args.verbose
        my_logger.info("\n\n%s TestKcfs: basePath=%s; kcfsPath=%s; count=%s; seed=%s" % (time.strftime("%Y-%m-%d %H:%M"), args.basepath, args.kcfspath, args.count, args.seed))
        fsrand.randomize()

    def __entry():
        try:
            main()
        except EnvironmentError, ex:
            fail(ex)
        except KeyboardInterrupt:
            fail("interrupted", 130)
    __entry()

