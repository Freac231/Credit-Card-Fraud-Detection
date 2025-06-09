import kagglehub

# Download latest version

path = kagglehub.dataset_download("joebeachcapital/credit-card-fraud")
print(f"Dataset downloaded: {path}")
