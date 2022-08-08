#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import logging

from Xcase.utils import get_xmind_testcase_list, xmind_testcase_to_json_file
from Xcase.utils import get_xmind_testsuite_list, xmind_testsuite_to_json_file
from Xcase.xmind2htp import xmind_to_htp_xlsx_file

logging.basicConfig(level=logging.INFO)


def main():
    xmind_file = 'docs/tcase.xmind'
    # xmind_file = '~/Desktop/迭代记录/Sprint 2022/Sprint Y22W01/「签约装修流程」.xmind'
    print('Start to convert XMind file: %s' % xmind_file)

    # 3、test dict/json data
    # (1) testsuite
    # testsuites = get_xmind_testsuite_list(xmind_file)
    # print('Convert XMind to testsuits dict data:\n%s' %
    #       json.dumps(testsuites, indent=2, separators=(',', ': '), ensure_ascii=False))
    #
    # # (2) testcase
    # testcases = get_xmind_testcase_list(xmind_file)
    # print('Convert Xmind to testcases dict data:\n%s' %
    #       json.dumps(testcases, indent=4, separators=(',', ': '), ensure_ascii=False))

    # (3) xmind file to htp excel
    xmind_to_htp_xlsx_file(xmind_file)
    xmind_testsuite_to_json_file(xmind_file)
    xmind_testcase_to_json_file(xmind_file)


if __name__ == '__main__':
    main()
