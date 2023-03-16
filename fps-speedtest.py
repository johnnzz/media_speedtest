#!/usr/bin/python3

import os
import time
import glob
#import io

reference_file = 'lossless-raw.nef'
run_time = 120

def clean_files():
	try:
		old_files = glob.glob('test-?????.nef')
		if old_files:
			print("removing old files")
			for old_file in old_files:
				os.remove(old_file)
	except Exception as err:
		pass

try:
	with open(reference_file, 'rb') as fh:
		test_image = fh.read()
	file_size = os.path.getsize(reference_file)
	print('read {} byte reference file, {}'.format(file_size, reference_file))
except Exception as err:
	print('cannot open {} due to {}'.format(reference_file, err))
	exit(1)

clean_files()

print('writing test files for {} seconds'.format(run_time))
file = 0
start_time = int(time.time())
until_time = start_time + run_time
while(int(time.time()) <= until_time):
	file += 1
	file_name = 'test-{0:05d}.nef'.format(file)
	with open(file_name, 'wb',0) as fh:
		fh.write(test_image)
end_time = int(time.time())
actual_seconds = end_time - start_time

clean_files()

fps = int(file / actual_seconds)
mbs = (fps * file_size) / 1048576

files_per_sec = int(actual_seconds / file)
print('wrote {} total files in {} seconds'.format(file, actual_seconds))
print('wrote {} files/seconds'.format(fps))
print('{} MB/s'.format(round(mbs, 2)))



