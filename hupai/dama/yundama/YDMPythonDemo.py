# -*- coding: cp936 -*-

import sys
import os
from ctypes import *

# ���ؽӿڷ�Ŀ¼ http://www.yundama.com/apidoc/YDM_SDK.html
# ����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html
# ���к������ѯ http://www.yundama.com/apidoc

print('>>>���ڳ�ʼ��...')

YDMApi = windll.LoadLibrary('yundamaAPI')

# 1. http://www.yundama.com/index/reg/developer ע�Ὺ�����˺�
# 2. http://www.yundama.com/developer/myapp ��������
# 3. ʹ����ӵ����ID����Կ���п��������ܷ��ֳ�

appId = 1   # ����ɣģ������߷ֳɱ�Ҫ��������¼�����ߺ�̨���ҵ��������ã�
appKey = c_char_p(b'22cc5376925e9387a23cf797cb9ba745')     # �����Կ�������߷ֳɱ�Ҫ��������¼�����ߺ�̨���ҵ��������ã�

print('����ɣģ�%d\r\n�����Կ��%s' % (appId, appKey))

# ע����������ͨ��Ա�˺ţ����ǿ������˺ţ�ע���ַ http://www.yundama.com/index/reg/user
# �����߿�����ϵ�ͷ���ȡ��ѵ������

username = c_char_p(b'slientcraft')
password = c_char_p(b'inwcwizard')

####################### һ��ʶ���� YDM_EasyDecodeByPath #######################

print('\r\n>>>����һ��ʶ��...')

# ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ��ڴ˲�ѯ�������� http://www.yundama.com/price.html
codetype = 6101

# ����30���ֽڴ��ʶ����
result = c_char_p(b"                              ")

# ʶ��ʱʱ�� ��λ����
timeout = 60

# ��֤���ļ�·��
filename = r'C:\Users\artof_000\Pictures\1.png'

# һ��ʶ������������� YDM_SetAppInfo �� YDM_Login���ʺϽű�����
# captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
#
# print("һ��ʶ����֤��ID��%d��ʶ������%s" % (captchaId, result))

################################################################################


########################## ��ͨʶ���� YDM_DecodeByPath #########################

print('\r\n>>>���ڵ�½...')

# ��һ������ʼ���ƴ��룬ֻ�����һ�μ���
YDMApi.YDM_SetAppInfo(appId, appKey)

# �ڶ�������½�ƴ����˺ţ�ֻ�����һ�μ���
uid = YDMApi.YDM_Login(username, password)

if uid > 0:

    print('>>>���ڻ�ȡ���...')

    # ��ѯ�˺�������Ҫ����
    balance = YDMApi.YDM_GetBalance(username, password)

    print('��½�ɹ����û�����%s��ʣ����֣�%d' % (username, balance))

    print('\r\n>>>������ͨʶ��...')

    # ����������ʼʶ��

    # ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ��ڴ˲�ѯ�������� http://www.yundama.com/price.html
    codetype = 6301

    # ����30���ֽڴ��ʶ����
    result = c_char_p(b"                              ")

    # ��֤���ļ�·��
    filename = c_char_p(b'C:\\Users\\artof_000\\Pictures\\1.png')

    # ��ͨʶ���������ȵ��� YDM_SetAppInfo �� YDM_Login ��ʼ��
    captchaId = YDMApi.YDM_DecodeByPath(filename, codetype, result)
    error =0
    str =''
    try:
        str =result._objects.decode("utf-8")
    except:
        error =1
    print("��ͨʶ����֤��ID��%d��ʶ������%s" % (captchaId, str))

else:
    print('��½ʧ�ܣ�������룺%d' % uid)

################################################################################

print('\r\n>>>����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html')

