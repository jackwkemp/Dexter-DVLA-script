def reset():
    from os import path

    with open("count.txt", "w+") as f:
        f.truncate(0)
        f.write("-1")

    if path.exists("raw_output.txt"):
        with open("raw_output.txt", "r+") as f:
            f.truncate(0)

    if path.exists("final_output.txt"):
        with open("final_output.txt", "r+") as f:
            f.truncate(0)


def main():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    import time
    import csv

    # Comment this out to reverse headless function
    options = Options()
    options.headless = True

    # Comment out 'options=options' to reverse headless function
    browser = webdriver.Chrome("/Users/ext04/Documents/Dexter/chromedriver", options=options)

    # Opens script on DVLA page
    browser.get("https://www.viewdrivingrecord.service.gov.uk/driving-record/licence-number")

    try:
        with open("count.txt", "r") as f:
            x = int(f.read())
            f.close()
    except IOError:
        with open("count.txt", "w") as f:
            f.write("0")
            f.close()
            x = 0

    x += 1
    y = (x + 1)

    with open("count.txt", "w") as f:
        f.write(str(x))

    # Kill switch
    with open("dexter_driver_list.csv") as f:
        rowcount = sum(1 for _ in f)
        kill = rowcount - 1
        if x == kill:
            post_process()

    # SHIFT + 'F6' to refactor
    # Sends data from 1st column to the Driver Licence box
    dlbar = browser.find_element_by_id("dln")
    with open("dexter_driver_list.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in list(csv_reader)[x:y]:
            dlbar.send_keys(str(line["Response 1"]).replace("{", "").replace("}", ""))
            time.sleep(3)

    # Sends data from 2nd column to the National Insurance Number box
    ninobar = browser.find_element_by_id("nino")
    with open("dexter_driver_list.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in list(csv_reader)[x:y]:
            ninobar.send_keys(str(line["Response 2"]).replace("{", "").replace("}", ""))
            time.sleep(3)

    # Sends data from 3rd column to the Postcode box
    pcbar = browser.find_element_by_id("postcode")
    with open("dexter_driver_list.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in list(csv_reader)[x:y]:
            pcbar.send_keys(str(line["Response 3"]).replace("{", "").replace("}", ""))
            time.sleep(3)

    # Clicks the 'I agree' tick box
    browser.find_element_by_id("dwpPermission").click()
    time.sleep(3)

    # Clicks the 'View now' button
    browser.find_element_by_id("submitDln").click()
    time.sleep(2)

    while True:
        try:
            browser.find_element_by_link_text("Penalties and disqualifications").click()
            time.sleep(2)

        except NoSuchElementException:
            # Notes if the driver entered their details incorrectly
            print("D", x, ",", "input error")
            with open("raw_output.txt", "a") as f:
                print("D", x, ",", "input error", file=f)
                browser.quit()
            main()

        else:
            pass
            # Saves the driver's current points to 'raw_output.txt'
            getpoints = browser.find_element_by_id("points")
            print("D", x, ",", getpoints.text)
            with open("raw_output.txt", "a") as f:
                print("D", x, ",", file=f)
                print(getpoints.text, file=f)
                browser.quit()
            main()


def post_process():
    import csv
    from os import path, remove

    bad_lines = ["You have", "To find out more", "Show information", "Start date:",
                 "Period:", "End date:", "Offence date:"
                 ]

    # Separate list needed to keep the line from deleting completely
    # e.g. '0 current penalty points' = '0 points'
    bad_words = ["current penalty "]

    # Removes unnecessary words and lines (above) and saves to another file
    with open("raw_output.txt", "r") as oldfile, open("lean_output.txt", "w") as newfile:
        for line in oldfile:
            for word in bad_words:
                line = line.replace(word, "")
            if not any(bad_line in line for bad_line in bad_lines):
                newfile.write(line)

    # Converts the previously 'leaned' output to a single line and saves it to another file
    with open("lean_output.txt", "r") as oldfile, open("singleline_output.txt", "w") as newfile:
        newfile.write(" ".join(line.strip() for line in oldfile))

    # Reorders the single line output
    with open("singleline_output.txt", "r") as oldfile, open("final_output.txt", "w") as newfile:
        reader = csv.reader(oldfile, delimiter="D", skipinitialspace=True)
        for row in reader:
            newfile.write("\n".join(row).lstrip())

    if path.exists("count.txt"):
        remove("count.txt")

    if path.exists("lean_output.txt"):
        remove("lean_output.txt")

    if path.exists("singleline_output.txt"):
        remove("singleline_output.txt")
        exit()


reset()

main()

post_process()
