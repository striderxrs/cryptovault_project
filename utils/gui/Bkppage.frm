VERSION 5.00
Begin VB.Form Backup 
   Caption         =   "Form2"
   ClientHeight    =   8910
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   13560
   LinkTopic       =   "Form2"
   Picture         =   "Bkppage.frx":0000
   ScaleHeight     =   8910
   ScaleWidth      =   13560
   StartUpPosition =   3  'Windows Default
   Begin VB.Label Label7 
      BackStyle       =   0  'Transparent
      Height          =   735
      Left            =   10560
      TabIndex        =   6
      Top             =   7800
      Width           =   2055
   End
   Begin VB.Label Label6 
      BackStyle       =   0  'Transparent
      Height          =   735
      Left            =   5400
      TabIndex        =   5
      Top             =   5640
      Width           =   2175
   End
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Height          =   735
      Left            =   5400
      TabIndex        =   4
      Top             =   4440
      Width           =   2175
   End
   Begin VB.Label Label4 
      BackStyle       =   0  'Transparent
      Height          =   855
      Left            =   5400
      TabIndex        =   3
      Top             =   3120
      Width           =   2175
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Height          =   735
      Left            =   960
      TabIndex        =   2
      Top             =   5640
      Width           =   2295
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Height          =   735
      Left            =   1080
      TabIndex        =   1
      Top             =   4440
      Width           =   2175
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Height          =   855
      Left            =   960
      TabIndex        =   0
      Top             =   3120
      Width           =   2295
   End
End
Attribute VB_Name = "Backup"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Declare Function ShellExecute Lib "shell32.dll" Alias "ShellExecuteA" (ByVal hWnd As Long, ByVal lpOperation As String, ByVal lpFile As String, ByVal lpParameters As String, ByVal lpDirectory As String, ByVal nShowCmd As Long) As Long
Const SW_SHOWNORMAL = 1
Private Sub Label1_Click()
Dim RetVal
RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\execdaily.bat", 1)
End Sub

Private Sub Label2_Click()
Dim RetVal2
RetVal2 = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\execweekly.bat", 1)
End Sub

Private Sub Label3_Click()
Dim RetVal3
RetVal3 = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\execmonthly.bat", 1)
End Sub
Private Sub Label4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)Handles Label4_Click()
System.Diagnostics.Process.Start ("C:\Users\Strider\Desktop\Cryptovault\s3-backup\backup_list\daily.s3")

End Sub

Private Sub Label7_Click()
Cryptovault.Show
Unload Me
End Sub
