# -*- coding:utf-8 -*-

import os
import sys
import k2engine

k2e = None
scan_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scan_result_value = [None, None, None, None, None, None, None, None, None, None]

def scan_callback(ret_value):
    try:
        scan_ctx = ret_value['context']
        scan_result[scan_ctx] = ret_value['result']
        scan_result_value[scan_ctx] = str(ret_value)
        
        print(ret_value['filename'])
        print(ret_value['result'])
        print(ret_value['virus_name'])
    except Exception as e:
        str(e)
        
# -------------------------------------------------------------------------
# 플러그인 엔진 로딩 실패 시 콜백 함수
# -------------------------------------------------------------------------
def import_error_callback(module_name):
    #global PLUGIN_ERROR
    #global g_options

    #if g_options.opt_debug:
        #if not PLUGIN_ERROR:
            #PLUGIN_ERROR = True
            print ('Invalid plugin: \'%s\'' % module_name)
            #print_error('Invalid plugin: \'%s\'' % module_name)

class k2Export:
    def __init__(self):
        self.k2 = None
        self.kav = [None, None, None, None, None, None, None, None, None, None]

    def k2_version(self, ctx):
        if self.kav[ctx] is None:
            return 'Context invalid!!!'

        return str(self.kav[ctx].get_version()).split(' ')[0] + '.' + str(self.kav[ctx].get_signum());

    def k2_load(self, ctx, plugins):
        if (ctx < 0) or (ctx > 9):
            return 0, 'Error: ctx overflow'
        try:
            self.k2 = k2engine.Engine()
            if not self.k2.set_plugins(os.path.abspath(plugins), import_error_callback):
                raise
            self.kav[ctx] = self.k2.create_instance()
            #self.kav[ctx].set_options(options)
            self.kav[ctx].init(import_error_callback)
        except Exception as e:
            return 0, str(e)
        return 1, ''

    def k2_scan(self, ctx, path):
        if self.kav[ctx] is None:
            return 0, 'Context invalid!!!'

        try:
            scan_result[ctx] = 0
            scan_result_value[ctx] = None
            self.kav[ctx].set_result()
            self.kav[ctx].scan(os.path.abspath(path), ctx, scan_callback)
        except Exception as e:
            return 0, str(e)
        return 1, ''

    def k2_result(self, ctx):
        return scan_result[ctx], scan_result_value[ctx]

    def k2_unload(self, ctx):
        if self.kav[ctx] is None:
            return
        self.kav[ctx].uninit()

def k2Init():
    global k2e
    global scan_result
    global scan_result_value
    k2e = k2Export()