# -*- coding: utf-8 -*-
"""DSM 6 SYNO.Core.System.Utilization data."""

DSM_6_CORE_UTILIZATION_ERROR_1055 = {
    "error": {
        "code": 1055,
        "errors": {
            "err_key": "",
            "err_line": 883,
            "err_msg": "Transmition failed.",
            "err_session": "",
        },
    },
    "success": False,
}

DSM_6_CORE_UTILIZATION = {
    "data": {
        "cpu": {
            "15min_load": 51,
            "1min_load": 37,
            "5min_load": 33,
            "device": "System",
            "other_load": 3,
            "system_load": 2,
            "user_load": 4,
        },
        "disk": {
            "disk": [
                {
                    "device": "sdc",
                    "display_name": "Drive 3",
                    "read_access": 3,
                    "read_byte": 55261,
                    "type": "internal",
                    "utilization": 12,
                    "write_access": 15,
                    "write_byte": 419425,
                },
                {
                    "device": "sda",
                    "display_name": "Drive 1",
                    "read_access": 3,
                    "read_byte": 63905,
                    "type": "internal",
                    "utilization": 8,
                    "write_access": 14,
                    "write_byte": 414795,
                },
                {
                    "device": "sdb",
                    "display_name": "Drive 2",
                    "read_access": 3,
                    "read_byte": 55891,
                    "type": "internal",
                    "utilization": 10,
                    "write_access": 15,
                    "write_byte": 415658,
                },
            ],
            "total": {
                "device": "total",
                "read_access": 9,
                "read_byte": 175057,
                "utilization": 10,
                "write_access": 44,
                "write_byte": 1249878,
            },
        },
        "lun": [],
        "memory": {
            "avail_real": 156188,
            "avail_swap": 4146316,
            "buffer": 15172,
            "cached": 2764756,
            "device": "Memory",
            "memory_size": 4194304,
            "real_usage": 24,
            "si_disk": 0,
            "so_disk": 0,
            "swap_usage": 6,
            "total_real": 3867268,
            "total_swap": 4415404,
        },
        "network": [
            {"device": "total", "rx": 109549, "tx": 45097},
            {"device": "eth0", "rx": 109549, "tx": 45097},
            {"device": "eth1", "rx": 0, "tx": 0},
        ],
        "space": {
            "total": {
                "device": "total",
                "read_access": 1,
                "read_byte": 27603,
                "utilization": 1,
                "write_access": 23,
                "write_byte": 132496,
            },
            "volume": [
                {
                    "device": "md2",
                    "display_name": "volume1",
                    "read_access": 1,
                    "read_byte": 27603,
                    "utilization": 1,
                    "write_access": 23,
                    "write_byte": 132496,
                }
            ],
        },
        "time": 1585503221,
    },
    "success": True,
}
