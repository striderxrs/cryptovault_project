VERSION 5.00
Begin VB.Form Cryptovault 
   Caption         =   "Form1"
   ClientHeight    =   8910
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   13560
   LinkTopic       =   "Form1"
   Picture         =   "Mainpage.frx":0000
   ScaleHeight     =   8910
   ScaleWidth      =   13560
   StartUpPosition =   3  'Windows Default
   Begin VB.Label clickrestore 
      BackStyle       =   0  'Transparent
      Height          =   1575
      Left            =   7320
      TabIndex        =   1
      Top             =   3840
      Width           =   4815
   End
   Begin VB.Label clickbackup 
      BackStyle       =   0  'Transparent
      Height          =   1575
      Left            =   1200
      TabIndex        =   0
      Top             =   3840
      Width           =   4815
   End
End
Attribute VB_Name = "Cryptovault"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub clickbackup_Click()
Backup.Show
Unload Me
End Sub

Private Sub clickrestore_Click()
Restore.Show
Unload Me
End Sub
