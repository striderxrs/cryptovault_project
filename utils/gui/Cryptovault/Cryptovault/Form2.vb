Public Class Form2

    Private Sub Label1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label1.Click
        'daily exec
        Dim RetVal
        RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\execdaily.bat", 1)
    End Sub

    Private Sub Label2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label2.Click
        'weekly exec
        Dim RetVal
        RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\execweekly.bat", 1)
    End Sub

    Private Sub Label3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label3.Click
        'monthly exec
        Dim RetVal
        RetVal = Shell("C:\Users\Strider\Desktop\Cryptovault\s3-backup\execmonthly.bat", 1)
    End Sub

    Private Sub Label7_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label7.Click
        CVmain.Show()
        Me.Hide()
    End Sub

    Private Sub Label4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label4.Click
        'open daily.s3
        System.Diagnostics.Process.Start("C:\Users\Strider\Desktop\Cryptovault\s3-backup\backup_list\daily.s3")
    End Sub

    Private Sub Label5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label5.Click
        'open weekly.s3"
        System.Diagnostics.Process.Start("C:\Users\Strider\Desktop\Cryptovault\s3-backup\backup_list\weekly.s3")
    End Sub

    Private Sub Label6_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label6.Click
        'open monthly.s3
        System.Diagnostics.Process.Start("C:\Users\Strider\Desktop\Cryptovault\s3-backup\backup_list\monthly.s3")
    End Sub
End Class