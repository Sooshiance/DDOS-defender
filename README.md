# DDOS Defender
It's just a simple ddos guard.

If you want to use this :

- first fill up some settings in `settings.py`
- change `MAX_LIMIT_REQUEST` value as you please.

<!-- I will add `time` object to the class,
to make server responsible after certain amount of time. -->

Time object added!


## Cache framework
You can add your cache framework in the `settings.py` to better controling 
over caching requests.
I'v added mine but, I make them comment, because the `cache_backends.py` file
does not configured.
You can configure the `cache_backends.py` as you please.

### Session
I will add details about session staff that if any request does not get a session,
It's probably comes from a malicious origin, so that request should be classified as 
a suspicious request.