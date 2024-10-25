from tenacity import retry, stop_after_attempt, wait_fixed
import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def with_circuit_breaker(func, *args, **kwargs):
    try:
        return breaker.call(func, *args, **kwargs)
    except pybreaker.CircuitBreakerError:
        return {"error": "Servicio no disponible"}
