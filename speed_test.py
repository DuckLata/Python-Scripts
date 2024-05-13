import speedtest

test = speedtest.Speedtest()

print("Loading server list...")

# This will gather a list of servers
test.get_servers()

# This will choose the best server
print("Choosing best server...")
best_server = test.get_best_server()
print(f"Server Located: {best_server['sponsor']}, located in {best_server['name']} {best_server['country']}")

# Checking the download speed
print("Performing download test...")
download_result = test.download()

# Checking the upload speed
print("Performing upload test...")
upload_result = test.upload()

# Checking the ping of the server
ping_result = test.results.ping

# Displaying all the results
print(f"Ping: {ping_result:.2f} ms\nDownload: {download_result/1024/1024:.2f} Mb/s\nUpload: {upload_result/1024/1024:.2f} Mb/s")