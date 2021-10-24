"""
hash table VS hash map VS hash set
hash set只有key 没有value, 去重的时候用
hash table 支持线程安全，可以多个线程同事调用一个hash table， 不会出问题 - which is used by Python dictionary
hash map不支持线程安全， 多个线程一起搞一个hash map会搞砸ps： 因为加锁和解锁很慢， 所以hash table会性能低一些


Open Hashing vs Closed Hashing
再好的 hash 函数也会存在冲突(Collision)
https://www.cs.usfca.edu/~galles/visualization/ClosedHash.html
https://www.cs.usfca.edu/~galles/visualization/OpenHash.html
"""