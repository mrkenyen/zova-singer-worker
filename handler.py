
import runpod

def handler(job):
    return {
        "status": "ok",
        "message": "ZOVA worker running",
        "input": job["input"]
    }

runpod.serverless.start({"handler": handler})
