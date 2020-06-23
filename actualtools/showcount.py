# 计算s1在s2中出现的次数
def get_show_count(s1, s2):
    c_num = s2.count(s1)
    print(c_num)
    return c_num



s1="&&"
# s2 = "##0293QN=20200623123000044;ST=31;CN=2011;PW=123456;MN=88888880000001;Flag=5;CP=&&DataTime=20200623123000;w80001-SampleTime=20200623122424,w80001-Rtd=6.400,w80001-Flag=N;w80002-SampleTime=20200623122424,w80002-Rtd=-0.900,w80002-Flag=N;w80004-SampleTime=2020"
s2 = "##0127QN=20200623122504356;ST=31;CN=2081;PW=123456;MN=88888880000001;Flag=5;CP=&&DataTime=20200623122504;RestartTime=20200623122342&&1100"
get_show_count(s1, s2)