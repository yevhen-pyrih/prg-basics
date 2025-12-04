import tv

TV = tv.TV

def main():
    tv = TV()

    tv.display_status()

    tv.turn_on()

    tv.display_status()

    tv.turn_off()

    tv.display_status()


if __name__ == "__main__":
    main()