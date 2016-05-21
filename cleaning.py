import pandas
import numpy
def data_cleaning(df):
    
    df = pandas.read_csv(df, index_col=False)

    df = pandas.DataFrame(df, columns = ['Date','Close'])
    df['Change'] = df['Close'] - df['Close'].shift()
    df['Change_Percentage'] = (df['Close'] - df['Close'].shift())/100
    
    df['Date'] = pandas.to_datetime(df['Date'])    
        
    ## PROC for 30 days
       
    df['PROC'] =  (df['Close'].shift(23) - df['Close'])/df['Close'].shift(23)
    print df    
        
    
   # RCI 
    
    delta = df['Change'].diff().dropna()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    u = delta * 0
    d = u.copy()
    period = 23
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    u[u.index[period-1]] = numpy.mean( u[:period] ) #first value is sum of avg gains
    u = u.drop(u.index[:(period-1)])
    d[d.index[period-1]] = numpy.mean( d[:period] ) #first value is sum of avg losses
    d = d.drop(d.index[:(period-1)])
    rs = pandas.stats.moments.ewma(u, com=period-1, adjust=False) / \
         pandas.stats.moments.ewma(d, com=period-1, adjust=False)
    df['rci'] = 100 - 100 / (1 + rs)
    
    date = pandas.datetime.now().date()
   
    
    df['days'] = (df['Date'] - date) / numpy.timedelta64(1, 'D')
    df = df.dropna()
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    print df
    df.to_csv('data.csv') 
    
if __name__ == '__main__':
    
    print data_cleaning('SENSEX.csv') 