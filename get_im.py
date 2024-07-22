import requests as req
import card
def get_imgs(name,number,name_imgs,path):
	if path == "":
		return "Failed no path entered"
	if path == "/" or path == "/home" :
		return "cannot save to root Or home!!"
	str_query = name
	n = int(number)
	url = "https://api.unsplash.com/photos/random"
	params = {
    "client_id": card.UNSPLASH_ACCESS_KEY,
    "count": n,
    "query": str_query
	}
	response = req.get(url, params)
	if response.status_code == 200:
		images = response.json()
		image_urls = [image["urls"]["regular"] for image in images] #راجع هذا
		for i,url in enumerate(image_urls,1):
			image_response = req.get(url)
			file_extension = url.split(".")[-1]
			file_name = f"{name_imgs}_{i}.jpeg"
			try:
				with open(f"{path}/{file_name}", "wb") as file:
					file.write(image_response.content)
					s = "Image saved"
			except FileNotFoundError:	
				return "this path doesnot exist"
		return s		
	else:
		return f"Error fetching {str_query} images:, {response.status_code}"
