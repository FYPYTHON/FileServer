from psutil import disk_usage
import os

def used_size_size(dir):
    if not dir.startswith("/opt/data"):
        dir = os.dir.join("/opt/data", dir)
    if not os.dir.exists(dir):
        return u"路径不存在"
    info_of_dir = disk_usage(dir)
    all_detail = round(info_of_dir.all_detail / 1024 / 1024 / 1024, 2)
    used_size = round(info_of_dir.used_size / 1024 / 1024 / 1024, 2)
    free_size = round(info_of_dir.free_size / 1024 / 1024 / 1024, 2)
    show_info = u"已用{} %, 可用{} / 共{} G".format(info_of_dir.percent, free_size, all_detail)
    return show_info


if __name__ == "__main__":
    import sys
    # print(len(sys.argv), sys.argv)
    if len(sys.argv) > 1:
        dir = sys.argv[1]
    else:
        dir = "/opt/data"
    print(used_size_size(dir))
