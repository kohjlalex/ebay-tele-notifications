# Streamlit app
st.title("Ebay Telegram Bot")

#st.header("Check which companies clear your requirements")

# Create a text input box for the user to enter strings
st.text("Enter your list of urls (separated by commas) below:")
urls_to_scrape = st.text_area("Input", height=5)

wishlist = []

pattern = r'www\.ebay\.com\.sg/itm/(\d+)(?:\?|$)'

split_list = urls_to_scrape.split(",") #for string in urls_to_scrape]

for url in split_list:
    match = re.search(pattern, url)

    if match:
        item_number = match.group(1)
        wishlist.append(item_number)
        print(item_number)
    else:
        print("No match found.")
