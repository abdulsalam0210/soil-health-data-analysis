{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9a424aad-bb75-431c-8723-dd97cf009b0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "There was an error managing msedgedriver (error sending request for url (https://msedgedriver.azureedge.net/LATEST_RELEASE_138_WINDOWS)); using driver found in the cache\n"
     ]
    },
    {
     "ename": "NoSuchElementException",
     "evalue": "Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"[id=\"ddlstate\"]\"}\n  (Session info: MicrosoftEdge=138.0.3351.121); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception\nStacktrace:\n\tGetHandleVerifier [0x0x7ff7cba681f5+23461]\n\t(No symbol) [0x0x7ff7cb9bc2e0]\n\tGetHandleVerifier [0x0x7ff7cbce0128+2611928]\n\t(No symbol) [0x0x7ff7cb7d91a8]\n\t(No symbol) [0x0x7ff7cb7d946b]\n\t(No symbol) [0x0x7ff7cb819a67]\n\t(No symbol) [0x0x7ff7cb7fa6ff]\n\t(No symbol) [0x0x7ff7cb7cf58d]\n\t(No symbol) [0x0x7ff7cb81754f]\n\t(No symbol) [0x0x7ff7cb7fa423]\n\t(No symbol) [0x0x7ff7cb7cea86]\n\t(No symbol) [0x0x7ff7cb7cdd11]\n\t(No symbol) [0x0x7ff7cb7ce8b3]\n\t(No symbol) [0x0x7ff7cb8cdd3d]\n\t(No symbol) [0x0x7ff7cb8db0c8]\n\tGetHandleVerifier [0x0x7ff7cbb4803b+940523]\n\tGetHandleVerifier [0x0x7ff7cbb50d91+976705]\n\t(No symbol) [0x0x7ff7cb9c9ed1]\n\t(No symbol) [0x0x7ff7cb9c28b4]\n\t(No symbol) [0x0x7ff7cb9c2a03]\n\t(No symbol) [0x0x7ff7cb9b44a6]\n\tBaseThreadInitThunk [0x0x7ffc4567e8d7+23]\n\tRtlUserThreadStart [0x0x7ffc460dc34c+44]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNoSuchElementException\u001b[0m                    Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 11\u001b[0m\n\u001b[0;32m      8\u001b[0m driver \u001b[38;5;241m=\u001b[39m webdriver\u001b[38;5;241m.\u001b[39mEdge()\n\u001b[0;32m      9\u001b[0m driver\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhttps://soilhealth.dac.gov.in/nutrient-dashboard\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 11\u001b[0m Select(driver\u001b[38;5;241m.\u001b[39mfind_element(By\u001b[38;5;241m.\u001b[39mID, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mddlstate\u001b[39m\u001b[38;5;124m\"\u001b[39m))\u001b[38;5;241m.\u001b[39mselect_by_visible_text(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBihar\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     12\u001b[0m time\u001b[38;5;241m.\u001b[39msleep(\u001b[38;5;241m2\u001b[39m)\n\u001b[0;32m     13\u001b[0m Select(driver\u001b[38;5;241m.\u001b[39mfind_element(By\u001b[38;5;241m.\u001b[39mID, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mddldistrict\u001b[39m\u001b[38;5;124m\"\u001b[39m))\u001b[38;5;241m.\u001b[39mselect_by_visible_text(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSiwan\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:922\u001b[0m, in \u001b[0;36mWebDriver.find_element\u001b[1;34m(self, by, value)\u001b[0m\n\u001b[0;32m    919\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m NoSuchElementException(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot locate relative element with: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mby\u001b[38;5;241m.\u001b[39mroot\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    920\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m elements[\u001b[38;5;241m0\u001b[39m]\n\u001b[1;32m--> 922\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mexecute(Command\u001b[38;5;241m.\u001b[39mFIND_ELEMENT, {\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124musing\u001b[39m\u001b[38;5;124m\"\u001b[39m: by, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m: value})[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:454\u001b[0m, in \u001b[0;36mWebDriver.execute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    451\u001b[0m response \u001b[38;5;241m=\u001b[39m cast(RemoteConnection, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcommand_executor)\u001b[38;5;241m.\u001b[39mexecute(driver_command, params)\n\u001b[0;32m    453\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response:\n\u001b[1;32m--> 454\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39merror_handler\u001b[38;5;241m.\u001b[39mcheck_response(response)\n\u001b[0;32m    455\u001b[0m     response[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unwrap_value(response\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    456\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py:232\u001b[0m, in \u001b[0;36mErrorHandler.check_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    230\u001b[0m         alert_text \u001b[38;5;241m=\u001b[39m value[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124malert\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    231\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace, alert_text)  \u001b[38;5;66;03m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[39;00m\n\u001b[1;32m--> 232\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace)\n",
      "\u001b[1;31mNoSuchElementException\u001b[0m: Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"[id=\"ddlstate\"]\"}\n  (Session info: MicrosoftEdge=138.0.3351.121); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception\nStacktrace:\n\tGetHandleVerifier [0x0x7ff7cba681f5+23461]\n\t(No symbol) [0x0x7ff7cb9bc2e0]\n\tGetHandleVerifier [0x0x7ff7cbce0128+2611928]\n\t(No symbol) [0x0x7ff7cb7d91a8]\n\t(No symbol) [0x0x7ff7cb7d946b]\n\t(No symbol) [0x0x7ff7cb819a67]\n\t(No symbol) [0x0x7ff7cb7fa6ff]\n\t(No symbol) [0x0x7ff7cb7cf58d]\n\t(No symbol) [0x0x7ff7cb81754f]\n\t(No symbol) [0x0x7ff7cb7fa423]\n\t(No symbol) [0x0x7ff7cb7cea86]\n\t(No symbol) [0x0x7ff7cb7cdd11]\n\t(No symbol) [0x0x7ff7cb7ce8b3]\n\t(No symbol) [0x0x7ff7cb8cdd3d]\n\t(No symbol) [0x0x7ff7cb8db0c8]\n\tGetHandleVerifier [0x0x7ff7cbb4803b+940523]\n\tGetHandleVerifier [0x0x7ff7cbb50d91+976705]\n\t(No symbol) [0x0x7ff7cb9c9ed1]\n\t(No symbol) [0x0x7ff7cb9c28b4]\n\t(No symbol) [0x0x7ff7cb9c2a03]\n\t(No symbol) [0x0x7ff7cb9b44a6]\n\tBaseThreadInitThunk [0x0x7ffc4567e8d7+23]\n\tRtlUserThreadStart [0x0x7ffc460dc34c+44]\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import Select, WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "import pandas as pd\n",
    "import time\n",
    "\n",
    "driver = webdriver.Edge()\n",
    "driver.get(\"https://soilhealth.dac.gov.in/nutrient-dashboard\")\n",
    "\n",
    "Select(driver.find_element(By.ID, \"ddlstate\")).select_by_visible_text(\"Bihar\")\n",
    "time.sleep(2)\n",
    "Select(driver.find_element(By.ID, \"ddldistrict\")).select_by_visible_text(\"Siwan\")\n",
    "time.sleep(2)\n",
    "Select(driver.find_element(By.ID, \"ddlblock\")).select_by_visible_text(\"Barharia\")\n",
    "time.sleep(2)\n",
    "Select(driver.find_element(By.ID, \"ddlCycle\")).select_by_visible_text(\"2023-24\")\n",
    "driver.find_element(By.ID, \"btnSubmit\").click()\n",
    "\n",
    "# Wait until table loads with data\n",
    "WebDriverWait(driver, 20).until(\n",
    "    EC.presence_of_element_located((By.ID, \"GridView1\"))\n",
    ")\n",
    "\n",
    "table = driver.find_element(By.ID, \"GridView1\")\n",
    "print(\"✅ Table Found\")\n",
    "print(\"Preview of table text:\")\n",
    "print(table.text)\n",
    "\n",
    "rows = table.find_elements(By.TAG_NAME, \"tr\")\n",
    "data = []\n",
    "\n",
    "for row in rows:\n",
    "    cols = row.find_elements(By.TAG_NAME, \"td\")\n",
    "    if cols:\n",
    "        data.append([col.text for col in cols])\n",
    "\n",
    "# Save to CSV if data found\n",
    "if data:\n",
    "    df = pd.DataFrame(data)\n",
    "    df.to_csv(\"nutrients_output.csv\", index=False)\n",
    "    print(\"✅ Data saved to CSV\")\n",
    "else:\n",
    "    print(\"❌ No data rows found\")\n",
    "\n",
    "driver.quit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fead4bc5-4247-4b02-b6ea-0e0ec0f62d58",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
