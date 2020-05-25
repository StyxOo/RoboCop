import tkinter as tk
import api_wrapper as wrapper


def save_config():
    wrapper.set_ip(ip_input.get())
    wrapper.set_port(port_input.get())
    wrapper.set_url(url_input.get())
    wrapper._write_config()
    window.destroy()


window = tk.Tk()

headline = tk.Label(text="Robotic hand api configuration")
headline.grid(row=0, column=0, columnspan=2)

ip_label = tk.Label(text="IP:", anchor='e')
ip_label.grid(row=1, column=0)
ip_input = tk.Entry()
ip_input.insert(0, wrapper._config['ip'])
ip_input.grid(row=1, column=1)

port_label = tk.Label(text="Port:", anchor='e')
port_label.grid(row=2, column=0)
port_input = tk.Entry()
port_input.insert(0, wrapper._config['port'])
port_input.grid(row=2, column=1)

url_label = tk.Label(text="URL:", anchor='e')
url_label.grid(row=3, column=0)
url_input = tk.Entry()
url_input.insert(0, wrapper._config['url'])
url_input.grid(row=3, column=1)

save_button = tk.Button(text="Save", width=20, height=3, command=save_config)
save_button.grid(row=4, column=0, columnspan=2)


if __name__ == '__main__':
    window.mainloop()
