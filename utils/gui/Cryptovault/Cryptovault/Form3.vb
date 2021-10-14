Public Class Form3

    Private Sub Label5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label5.Click
        'back button
        CVmain.Show()
        Me.Hide()
    End Sub

    Private Sub Label2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label2.Click
        'custom browse
        Dim RetVal
        RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\restore_browse_files_help.bat", 1)
        Clipboard.SetText("cd C:\Users\Strider\Desktop\Cryptovault\s3-backup")
    End Sub

    Private Sub Label4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label4.Click
        'custom restore
        Dim RetVal
        RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\restore_full_restore_help.bat", 1)
        Clipboard.SetText("cd C:\Users\Strider\Desktop\Cryptovault\s3-backup")
    End Sub

    'Private Sub Label1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
    'browse last archive (daily)
    'Dim RetVal
    ' RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\browse_recent.bat", 1)
    ' Clipboard.SetText("C:\Users\Strider\Desktop\Cryptovault\s3-backup\s3restore.py browse-files -s daily -d")
    'End Sub

    Private Sub Label3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label3.Click
        'restore last archive (daily)
        Dim RetVal
        RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\restore_recent.bat", 1)
    End Sub
End Class