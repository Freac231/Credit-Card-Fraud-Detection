import kagglehub

# Download latest version
path = ''

if __name__ == "__main__":
    path = kagglehub.dataset_download("joebeachcapital/credit-card-fraud")
    print(f"Dataset downloaded: {path}")
