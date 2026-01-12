param([string]$name, [string]$surname)

# Function to check if an Active Directory user account exists based on given name and surname
function Get-ADUserDetails {
    param (
        [string]$GivenName,
        [string]$Surname
    )
    $user = Get-ADUser -Filter { GivenName -eq $GivenName -and Surname -eq $Surname } -Properties *
    return $user
}

# Call the function to get the user account details
$userAccount = Get-ADUserDetails -GivenName $name -Surname $surname

# Check if the user account exists and display details
if ($userAccount) {
    $userAccount | Select-Object Name, SamAccountName, DistinguishedName, Enabled, Created, Description
}