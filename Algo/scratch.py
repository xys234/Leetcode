
import pandas as pd
import os

DATA_DIR = r"X:\Non_VDOT\WMATA_JD_MD\JD_RTSP\2040_Base_Branch"
ACCESS_FILE = os.path.join(DATA_DIR,'Walkacc.txt')

def find_field(rec, field_name):
    for i, f in enumerate(rec):
        if field_name in f:
            return i


def read_to_dict(file):
    out = []
    with open(file, 'r') as f:
        for l in f:

            data = l.split()

            # find the field
            zone_field_ind = find_field(data, "N=")
            mode_field_ind = find_field(data, 'MODE=')
            speed_field_ind = find_field(data, 'SPEED=')
            oneway_field_ind = find_field(data, 'ONEWAY=')
            dist_field_ind = find_field(data, 'DIST=')

            zone_pair = data[zone_field_ind].split("=")[1]
            from_zone = int(zone_pair.split("-")[0])
            to_zone = int(zone_pair.split("-")[1])

            mode = int(data[mode_field_ind].split("=")[1])
            speed = float(data[speed_field_ind].split("=")[1])
            oneway = data[oneway_field_ind].split("=")[1]
            dist = float(data[dist_field_ind].split("=")[1])

            out.append(dict(from_zone=from_zone, to_zone=to_zone, oneway=oneway, mode=mode, speed=speed, dist=dist))

    return out



if __name__=='__main__':
    read_to_dict(ACCESS_FILE)