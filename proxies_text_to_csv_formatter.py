import pandas as pd


def proxies_text_to_csv(data):

    df = pd.read_table(data,
                       sep=':',
                       header=None,
                       names=['ip',
                              'port',
                              'proxy-username',
                              'proxy-password',
                              'accounts',
                              'rotate'])

    ip_and_port = df.iloc[:, 0].map(str) + ':' + df.iloc[:, 1].map(str)
    df.insert(0, 'proxy-ip:port', ip_and_port)
    df.drop(['ip', 'port'], axis=1, inplace=True)
    df.to_csv('./result.csv', index=False)

    return df


if __name__ == '__main__':
    data = 'D:/公司社交媒体运维/Webshare Proxies/Webshare 70 proxies.txt'
    proxies_text_to_csv(data)