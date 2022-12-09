from urllib import request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scanner import *
from gspread_formatting import *
from googleapiclient import discovery
from Google import *



#Header Lists
bank_header_list = ["Transaction Date", "Description", "Amount", "Running Bal"]

#defining the scope of the application
scope_app = ["https://www.googleapis.com/auth/spreadsheets"] 

#credentials to the account
cred = ServiceAccountCredentials.from_json_keyfile_name("win_finance_credentials.json",scope_app) 

#secret JSON File
secret_file = "win_OAuth.json"

#spreadsheet_id
spreadsheet_id = "1Ok7bCIplJnvrLn8ltPFJrG9YxOpbeTvQzVrXoEsWPI4"

# authorize the clientsheet 
client = gspread.authorize(cred)

def Connect_to_GSpread():
    #Connecting to Google Sheets
    #------------------------------------------
    # defining the scope of the application
    scope_app =["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"] 

    #credentials to the account
    cred = ServiceAccountCredentials.from_json_keyfile_name("win_finance_credentials.json",scope_app) 

    # authorize the clientsheet 
    client = gspread.authorize(cred)
    #------------------------------------------

    # Open the spreadsheet
    sh = client.open("Personal Finance")
    
    print(sh)
    return sh

#Creates a new worksheet with each Month
def Format_Gspread(file_name):
    sh = Connect_to_GSpread()
    worksheet = sh.worksheet(file_name)

#=======================================================
#Fomatting Col / Row Sizes
    set_column_width(worksheet, "A", 90)
    set_column_width(worksheet, "B", 300)
    set_column_width(worksheet, "C", 70)
    set_column_width(worksheet, "D", 150)
    set_column_width(worksheet, "E", 150)
    set_column_width(worksheet, "F", 150)
    set_column_width(worksheet, "G", 150)
    set_column_width(worksheet, "H", 150)

#=======================================================
#Setting up the Text Format 
    # worksheet.format("A1:D1", {
    #     "bold" : True

    # })

#CSV Colors
    fmt = CellFormat(
        #Bright Orange 255, 172, 28
        backgroundColor=color(1, 0.67, 0.11),
        textFormat=TextFormat(bold = True)
    )

    format_cell_range(worksheet, "A1:C1", fmt)

    #Types of Transactions
    fmt = CellFormat(
      #Grey 204 204 204
        backgroundColor=color(0.8, 0.8, 0.8),
        textFormat=TextFormat(bold = True)
    )

    format_cell_range(worksheet, "D1:H1", fmt)

#Updating the information stored in PD into Gspread
def Update_PD_Worksheet(file_name):
    from CSV_Operations import Update_Last_Row_CSV
    sh = Connect_to_GSpread()
    worksheet = sh.add_worksheet(file_name, rows = 60, cols = 60)
    
#Setting up the Information Template
    df = Update_Last_Row_CSV(file_name)
    df = df.fillna('')
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

#Gets the title of each worksheet from GSpread 
def Title_Worksheet_List():  
    title_list = []
    sh = Connect_to_GSpread()
    worksheet_list = sh.worksheets()

    for ws in worksheet_list:
        title_list.append(ws.title)

    return title_list

#Checks the Common Sheets between CSV and GSpread and remove it 
def Common_Sheet(worksheet_list, file_list):
    i = 0
    while i < len(worksheet_list):
        j = 0
        while j < len(file_list):
            if file_list[j] == worksheet_list[i]:
                file_list.remove(file_list[j])
            j = j + 1
        
        i = i + 1

    return file_list

def Pie_Chart():
    from pprint import pprint
    from googleapiclient import discovery

    # TODO: Change placeholder below to generate authentication credentials. See
    # https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
    #
    # Authorize using one of the following scopes:
    #     'https://www.googleapis.com/auth/drive'
    #     'https://www.googleapis.com/auth/drive.file'
    #     'https://www.googleapis.com/auth/spreadsheets'
    credentials = None

    service = discovery.build('sheets', 'v4', credentials=cred)

    # The spreadsheet to apply the updates to.
    sh_id = "1Ok7bCIplJnvrLn8ltPFJrG9YxOpbeTvQzVrXoEsWPI4"
    spreadsheet_id = "2021772043"
    sheet_ID = "1676022265"



    batch_update_spreadsheet_request_body = {
        # A list of updates to apply to the spreadsheet.
        # Requests will be applied in the order they are specified.
        # If any request is not valid, no requests will be applied.
        'requests': [
          {
          "addChart":{
            "chart":{
              "spec":{
                "title" : "Spending Types",
                "basicChart": {
                  "chartType" : "COLUMN",
                  "legendPosition" : "BOTTOM_LEGEND",
                  "axis" : [{
                    "position" : "BOTTOM_AXIS",
                    "title" : "Types of Cost"
                  },
                  {
                    "position" : "LEFT_AXIS",
                    "title" : "Cost"
                  }
                  ],

                  "domains": [
                {
                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 0, #Col A
                          "endColumnIndex": 1
                        }
                      ]
                    }
                  },
                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 1, #Col B
                          "endColumnIndex": 2
                        }
                      ]
                    }
                  },
                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 2, #Col C
                          "endColumnIndex": 3
                        }
                      ]
                    }
                  },

                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 3, #Col D
                          "endColumnIndex": 4
                        }
                      ]
                    }
                  },

                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 4, #Col E
                          "endColumnIndex": 5
                        }
                      ]
                    }
                  },

                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 5, #Col F
                          "endColumnIndex": 6
                        }
                      ]
                    }
                  },

                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 6, #Col G
                          "endColumnIndex": 7
                        }
                      ]
                    }
                  },

                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, #Row 1
                          "endRowIndex": 1,
                          "startColumnIndex": 7, #Col H
                          "endColumnIndex": 8
                        }
                      ]
                    }
                  },
                }
              ],
              "series": [
                {
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 1, 
                          "endRowIndex": 2,
                          "startColumnIndex": 0, #Col A 
                          "endColumnIndex": 1
                        }
                      ]
                    }
                  },
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 0, 
                          "endRowIndex": 2,
                          "startColumnIndex": 1, #Col B
                          "endColumnIndex": 2
                        }
                      ]
                    }
                  },
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 1, 
                          "endRowIndex": 2,
                          "startColumnIndex": 2, #Col C
                          "endColumnIndex": 3
                        }
                      ]
                    }
                  },
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 1, 
                          "endRowIndex": 2,
                          "startColumnIndex": 3, #Col D
                          "endColumnIndex": 4
                        }
                      ]
                    }
                  },
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 1, 
                          "endRowIndex": 2,
                          "startColumnIndex": 4, #Col E
                          "endColumnIndex": 5
                        }
                      ]
                    }
                  },
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 1, 
                          "endRowIndex": 2,
                          "startColumnIndex": 5, #Col F
                          "endColumnIndex": 6
                        }
                      ]
                    }
                  },
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 1, 
                          "endRowIndex": 2,
                          "startColumnIndex": 6, #Col G
                          "endColumnIndex": 7
                        }
                      ]
                    }
                  },
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": spreadsheet_id,
                          "startRowIndex": 1, 
                          "endRowIndex": 2,
                          "startColumnIndex": 7, #Col H
                          "endColumnIndex": 8
                        }
                      ]
                    }
                  },
                  "targetAxis": "LEFT_AXIS"
                },
                
              ],
              "headerCount" : 1
                }
              },
              "position" : {
                "overlayPosition": {
                  "anchorCell": {
                    "sheetId": sheet_ID,
                    "rowIndex": 2,
                    "columnIndex": 2
                  },
                  "offsetXPixels": 50,
                  "offsetYPixels": 50
                }
              }
            }
          }
        }
        ],  # TODO: Update placeholder value.
        
        # TODO: Add desired entries to the request body.
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=sh_id, body=batch_update_spreadsheet_request_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    pprint(response)

def Adding_Total(file_name):
  print("In Progress")

def Final_List():
  raw_worksheet = Title_Worksheet_List()
  print(file_list)
  print(raw_worksheet)
  final_list = Common_Sheet(raw_worksheet, file_list)

  return final_list

def Run_Finance():
  final_list = Final_List()
  i = 0

  #Pie_Chart(file_list, 53)

  #Start Updating All the CSV Files onto GSpread
  while i < len(final_list):
      Update_PD_Worksheet(final_list[i])
      Format_Gspread(final_list[i])
      i = i + 1 
#=======================================================

Run_Finance()
#Connect_to_GSpread()
#Pie_Chart()
# API_NAME = "sheets"
# API_VERS = "v4"
# service = Create_Service(secret_file, API_NAME, API_VERS, scope_app)