from api_wrapper import wrapper

if __name__ == '__main__':
    print(wrapper._config)
    wrapper.set_use_save_connection(False)
    print(wrapper._config)
    print(wrapper._create_request_url())
