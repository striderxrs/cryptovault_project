VERSION 5.00
Begin VB.Form Restore 
   Caption         =   "Form3"
   ClientHeight    =   8910
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   13560
   LinkTopic       =   "Form3"
   Picture         =   "restorepage.frx":0000
   ScaleHeight     =   8910
   ScaleWidth      =   13560
   StartUpPosition =   3  'Windows Default
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Height          =   735
      Left            =   10560
      TabIndex        =   4
      Top             =   7680
      Width           =   2055
   End
   Begin VB.Label Label4 
      BackStyle       =   0  'Transparent
      Height          =   975
      Left            =   7320
      TabIndex        =   3
      Top             =   5280
      Width           =   4455
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Height          =   975
      Left            =   7320
      TabIndex        =   2
      Top             =   3360
      Width           =   4455
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Height          =   855
      Left            =   1200
      TabIndex        =   1
      Top             =   5280
      Width           =   4335
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Height          =   855
      Left            =   1200
      TabIndex        =   0
      Top             =   3480
      Width           =   4335
   End
End
Attribute VB_Name = "Restore"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Label1_Click()

End Sub

Private Sub Label5_Click()
Cryptovault.Show
Unload Me
End Sub
