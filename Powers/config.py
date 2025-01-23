from os import getenv

# if using getenv: getenv("ENV VARIABLE NAME", "Default value") getenv should be in this format if it is like getenv("API_HASH") add your value by adding comma like getenv("API_HASHH", "My api hash")
# also if getenv have int type conversion leave it for example if it is like int(getenv(....)) leave it
# If I ask to remove int you have to do change it from this int(getenv(...)) to this getenv(...) 

API_ID = 20628383  # This should be without anhhy quotation as it is integer
API_HASH = "65a242463b8af9ba7b3c41d8de9738d1" #This should be inside the quotation as it is string
BOT_TOKEN = "7288449922:AAFN6-fW8oK_JcS12T2ZJdvWi4bs5aysH9c" # Same here
SUDO = [int(i.strip()) for i in getenv("SUDO", "1432756163 1344569458 1446111611 682111519").strip().split()]
OWNER_ID = int(getenv("OWNER","1446111611"))
FSUB_CHANNEL = [int(i.strip())
                for i in getenv("FSUB_CHANNEL", "").strip().split()]
REQ_FSUB = [int(i.strip()) for i in getenv("REQ_FSUB", "").strip().split()]
AUTO_DEL = int(getenv("AUTO_DEL_TIME", 720))
AUTO_DEL_IN = getenv("AUTO_DEL_IN", "minute").lower()
START_PIC = getenv(
    "START_PIC", "https://envs.sh/gNn.jpg")
DB_URI = "mongodb+srv://utahheroku10:utahheroku10@cluster0.lt5bp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
SEARCH_PIC = "https://envs.sh/gNT.jpg"
NO_RES_PIC = "https://envs.sh/gNp.jpg"
TRENDING = "https://envs.sh/gNA.jpg"
