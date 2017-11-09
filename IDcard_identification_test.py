#  -*- coding: utf-8 -*-
from ID_Card_verifier import *
import pickle
tstdict={'longerr':'3306811995020103391',
         'regionerr':'100681199502010339',
         'illegalstr':'330681199502010B39',
         'birtherr':'330681199951312025',
         'verifyerr':'330681199502010338',
         'pass':'330681199502010339',
         'sex':'330681199502010339',
         'sex1':'330681199502010349',
         'sex_15':'330681950201033'
         }

resultmessage={'pass':'correct',
              'errtype1':'long incorrect',
              'errtype2':'region incorrect',
              'errtype3':'date incorrect',
              'errtype4':'verify incorrect',
               'female':'female',
               'male':'male'
               }

testloglst=[]


def savelog(asrt_res,res,method, id):
    testlog={}
    testlog['asrt_res']=asrt_res
    testlog['res']=res
    testlog['test_func']=method
    testlog['test_id']=id

    print testlog
    print testloglst
    testloglst.append(testlog)
    print testloglst
    with open('idcard_identification_testlog.pkl', 'r+') as pickle_file:

        pickle.dump(testloglst, pickle_file)




class Testmethod(object):
    def __get__(self,ist,tstclass):
        return ist.asrt_eq(tstclass.method[0](ist.id))

class TestId(object):
    def __init__(self,id,asrt_res):
        self.id=id
        self.asrt_res=asrt_res


    test = Testmethod()

    def asrt_eq(self,res):
        savelog(self.asrt_res, res, self.method[0].__name__, self.id)
        assert self.asrt_res==res

    @classmethod
    def setmethod(cls,method):
        cls.method=[]
        cls.method.append(method)


class TestIDlong(TestId):
    def __init__(self, id ,asrt_res):
        TestId.__init__(self, id, asrt_res)

class TestIDregion(TestId):
    def __init__(self, id, asrt_res):
        TestId.__init__(self, id, asrt_res)

class TestIDbirth(TestId):
    def __init__(self, id, asrt_res):
        TestId.__init__(self, id, asrt_res)



class TestIDverify(TestId):
    def __init__(self, id, asrt_res):
        TestId.__init__(self, id, asrt_res)



class TestIDSex(TestId):
    def __init__(self, id, asrt_res):
        TestId.__init__(self, id, asrt_res)

def setmethod():
    TestIDlong.setmethod(checkLen)
    TestIDregion.setmethod(checkCity)
    TestIDbirth.setmethod(checkDate)
    TestIDverify.setmethod(checkByte)
    TestIDSex.setmethod(checkSex)

def testall():

    s = TestIDlong(tstdict['longerr'], resultmessage['errtype1'])
    s.test

    s = TestIDregion(tstdict['regionerr'], resultmessage['errtype2'])
    s.test

    s = TestIDbirth(tstdict['birtherr'], resultmessage['errtype3'])
    s.test

    s = TestIDbirth(tstdict['illegalstr'], resultmessage['errtype3'])
    s.test #checkDate 也被用于校验非法字符串，之后会修正

    s = TestIDverify(tstdict['regionerr'], resultmessage['errtype4'])
    s.test

    s = TestIDSex(tstdict['sex'], resultmessage['male'])
    s.test

    s = TestIDSex(tstdict['sex1'], resultmessage['female'])
    s.test

    s = TestIDSex(tstdict['sex_15'], resultmessage['male'])
    s.test







if __name__ == '__main__':
    setmethod()
testall()