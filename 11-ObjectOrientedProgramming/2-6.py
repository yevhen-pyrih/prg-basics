import phone

Phone = phone.Phone

def main():
    phone = Phone(5200, "good", "1234")

    phone.start_operating()

if __name__ == "__main__":
    main()