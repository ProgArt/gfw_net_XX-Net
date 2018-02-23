
import xconfig


class ConfigBase(xconfig.Config):
    def set_default(self):
        # proxy
        self.set_var("PROXY_ENABLE", 0)
        self.set_var("PROXY_TYPE", "HTTP")
        self.set_var("PROXY_HOST", "")
        self.set_var("PROXY_PORT", 0)
        self.set_var("PROXY_USER", "")
        self.set_var("PROXY_PASSWD", "")

        # http_dispatcher
        self.set_var("dispather_min_idle_workers", 0)
        self.set_var("dispather_work_min_idle_time", 0)
        self.set_var("dispather_work_max_score", 20000)
        self.set_var("dispather_max_workers", 60)

        # http 1.1 worker
        self.set_var("http1_first_ping_wait", 300)
        self.set_var("http1_ping_interval", 300)
        self.set_var("http1_idle_time", 360)
        self.set_var("http1_max_process_tasks", 99999999)

        # http 2 worker
        self.set_var("http2_max_concurrent", 60)
        self.set_var("http2_max_timeout_tasks", 5)
        self.set_var("http2_status_to_close", [])

        # worker_base
        self.set_var("show_state_debug", 0)

        # connect manager
        self.set_var("https_max_connect_thread", 1)
        self.set_var("max_connect_thread", 1)
        self.set_var("ssl_first_use_timeout", 10)
        self.set_var("connection_pool_min", 1)
        self.set_var("https_keep_alive", 15)
        self.set_var("https_connection_pool_min", 1)
        self.set_var("https_connection_pool_max", 2)
        self.set_var("https_new_connect_num", 1)
        self.set_var("http1_new_connect_num", 1)

        # connect_creator
        self.set_var("connect_force_http2", 0)

        # ip manager
        self.set_var("check_exist_ip_on_startup", 0)
        self.set_var("auto_adjust_scan_ip_thread_num", 1)
        self.set_var("max_scan_ip_thread_num", 0)
        self.set_var("max_good_ip_num", 3000)
        self.set_var("max_links_per_ip", 1)
        self.set_var("ip_connect_interval", 5)
        self.set_var("record_ip_history", 0)
        self.set_var("down_fail_connect_interval", 60)
        self.set_var("long_fail_threshold", 300)
        self.set_var("long_fail_connect_interval", 180)
        self.set_var("short_fail_connect_interval", 10)

        # ip source
        self.set_var("use_ipv6", "auto") #
        self.set_var("ipv6_scan_ratio", 0.5)