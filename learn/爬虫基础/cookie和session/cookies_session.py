'''
cookies：
    http是无状态服务，不会记录用户状态信息，也不会记住客户端是否访问过
    cookies可以记录客户端登录信息，客户端再次访问时携带上cookies，服务端就会通过客户端的访问
    cookies存在客户端可能会被删除，信息会丢失
    cookies在浏览器中记录信息是不安全的，不能记录敏感信息
session：
    session存在于客户端
    为每个用户生成一个sessionid
    并把sessionID设置在浏览器中



'''