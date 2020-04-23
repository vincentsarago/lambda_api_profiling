# FastAPI+Mangum Vs lambda-proxy

Simple and stupid profiling between lambda-proxy Vs FastAPI+Mangum app.

We use lambda-proxy for most of our lambda based project, but FastAPI+Mangum is a really nice solution to built architecture agnostic app. The goal of this profiling was just to get a better understanding of the performances between both solution.

### Module Import + Get Call
```
$ python test.py 

FastAPI + Mangum
         448158 function calls (422332 primitive calls) in 0.403 seconds

   Ordered by: internal time
   List reduced from 2764 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      421    0.035    0.000    0.035    0.000 {built-in method marshal.loads}
1545/1539    0.025    0.000    0.106    0.000 {built-in method builtins.__build_class__}
    31/30    0.021    0.001    0.022    0.001 {built-in method _imp.create_dynamic}
  983/147    0.018    0.000    0.049    0.000 sre_parse.py:475(_parse)
     2456    0.015    0.000    0.015    0.000 {built-in method posix.stat}
      793    0.011    0.000    0.014    0.000 sre_compile.py:276(_optimize_charset)
      421    0.011    0.000    0.015    0.000 <frozen importlib._bootstrap_external>:914(get_data)
     1372    0.010    0.000    0.042    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
  9970/13    0.009    0.000    0.022    0.002 copy.py:132(deepcopy)
 2023/136    0.008    0.000    0.029    0.000 sre_compile.py:71(_compile)

LambdaProxy
         371838 function calls (368311 primitive calls) in 0.307 seconds

   Ordered by: internal time
   List reduced from 918 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      761    0.029    0.000    0.029    0.000 {built-in method posix.listdir}
     4477    0.020    0.000    0.020    0.000 {built-in method posix.stat}
     2661    0.012    0.000    0.031    0.000 version.py:198(__init__)
   422/69    0.009    0.000    0.029    0.000 sre_parse.py:475(_parse)
      696    0.007    0.000    0.035    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
    12391    0.007    0.000    0.007    0.000 sre_parse.py:233(__next)
     1362    0.006    0.000    0.017    0.000 version.py:131(_legacy_cmpkey)
       30    0.005    0.000    0.005    0.000 {built-in method marshal.loads}
     2664    0.005    0.000    0.005    0.000 {method 'search' of 're.Pattern' objects}
     1299    0.005    0.000    0.006    0.000 version.py:343(_cmpkey)
```

### Only GET call
```
$ python test_noimport.py

FastAPI + Mangum
         491 function calls (313 primitive calls) in 0.001 seconds

   Ordered by: internal time
   List reduced from 151 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     91/3    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
     91/3    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        2    0.000    0.000    0.001    0.000 base_events.py:1675(_run_once)
        5    0.000    0.000    0.000    0.000 routing.py:171(matches)
        1    0.000    0.000    0.001    0.001 adapter.py:82(handle_http)
        1    0.000    0.000    0.001    0.001 base_events.py:517(run_forever)
        1    0.000    0.000    0.000    0.000 base_events.py:393(create_task)
        1    0.000    0.000    0.000    0.000 encoder.py:204(iterencode)
        6    0.000    0.000    0.000    0.000 typing.py:809(__new__)
        1    0.000    0.000    0.000    0.000 utils.py:433(solve_dependencies)



LambdaProxy
         77 function calls in 0.000 seconds

   Ordered by: internal time
   List reduced from 41 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 proxy.py:643(__call__)
        2    0.000    0.000    0.000    0.000 encoder.py:204(iterencode)
        2    0.000    0.000    0.000    0.000 encoder.py:182(encode)
        1    0.000    0.000    0.000    0.000 proxy.py:425(_get_matching_args)
        1    0.000    0.000    0.000    0.000 proxy.py:150(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:183(dumps)
        5    0.000    0.000    0.000    0.000 re.py:271(_compile)
        1    0.000    0.000    0.000    0.000 __init__.py:1614(isEnabledFor)
        5    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
```