from main_app import MainApp
import logging_config
import logging


if __name__ == "__main__":
    logging_config.setup_logging()
    try:
        m = MainApp()
        m.mainloop()
    except FileNotFoundError as e:
        logging.error(f"File Not found {e}", exc_info=True)
