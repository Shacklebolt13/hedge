import psutil
import pandas


def analyzeNetwork():
    net=psutil.net_connections("all")
    result=pandas.DataFrame(net)
    
    result['name']=list(map(lambda x:psutil.Process(x).name(),result.pid))
    result.drop(['family','fd','type'],axis=1,inplace=True)
    raddrSplit=pandas.DataFrame(result.laddr.to_list(),index=result.index)
    
    result['lIP']=raddrSplit.ip
    result['port']=raddrSplit.port
    result.drop('laddr',axis=1,inplace=True)
    result.drop('pid',axis=1,inplace=True)
    

    raddrSplit=pandas.DataFrame(result.raddr.to_list(),index=result.index)
    result['rIP']=raddrSplit[0]
    result.drop('raddr',axis=1,inplace=True)


    result=result.loc[result.rIP!='127.0.0.1',:]

    return result


print(analyzeNetwork())