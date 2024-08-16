import psutil
import cpuinfo

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return f"{info['brand_raw']} - {info['hz_actual_friendly']}"

print("Загруженность процессора:", get_cpu_usage(), "%")


