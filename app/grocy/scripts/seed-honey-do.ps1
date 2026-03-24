param(
    [Parameter(Mandatory = $true)]
    [string]$ApiKey,

    [string]$BaseUrl = "http://192.168.86.47:9192"
)

$headers = @{
    "GROCY-API-KEY" = $ApiKey
    "Content-Type"  = "application/json"
}

function Invoke-GrocyPost {
    param(
        [Parameter(Mandatory = $true)]
        [string]$EntityType,

        [Parameter(Mandatory = $true)]
        [hashtable]$Data
    )

    $body = $Data | ConvertTo-Json -Depth 10 -Compress
    Invoke-RestMethod -Method Post -Uri "$BaseUrl/api/objects/$EntityType" -Headers $headers -Body $body
}

$taskCategoryNames = @("Ross", "Kelly")
$taskCategoryIds = @{}

foreach ($category in $taskCategoryNames) {
    $created = Invoke-GrocyPost -EntityType "task_categories" -Data @{
        name = $category
    }
    $taskCategoryIds[$category] = $created.created_object_id
}

$tasks = @(
    @{ name = "Kelly - Kitchen Countertops"; due_date = "2026-07-01"; category = "Kelly" },
    @{ name = "Ross - Basement Sliding Doors"; due_date = "2026-07-01"; category = "Ross" },
    @{ name = "Kelly - Mailbox Sign"; due_date = "2026-06-01"; category = "Kelly" },
    @{ name = "Ross - Bathtub Caulking"; due_date = "2026-08-01"; category = "Ross" },
    @{ name = "Ross - Recessed Lights"; due_date = "2026-10-01"; category = "Ross" },
    @{ name = "Ross - Upstairs Air Condition"; due_date = "2026-05-01"; category = "Ross" },
    @{ name = "Kelly - Kitchen Cabinet Painting"; due_date = "2026-05-01"; category = "Kelly" },
    @{ name = "Ross - Dining Room Cabinet Build"; due_date = "2026-06-15"; category = "Ross" },
    @{ name = "Kelly - Dining Room Cabinet Organization"; due_date = "2026-07-01"; category = "Kelly" },
    @{ name = "Kelly - Sell or Throw Away Wedding Decorations"; due_date = "2026-06-01"; category = "Kelly" },
    @{ name = "Kelly - Remove Clutter"; due_date = "2026-06-01"; category = "Kelly" }
)

foreach ($task in $tasks) {
    Invoke-GrocyPost -EntityType "tasks" -Data @{
        name = $task.name
        due_date = $task.due_date
        category_id = $taskCategoryIds[$task.category]
    } | Out-Null
}

$chores = @(
    @{ name = "Walk the Dog"; period_type = "daily"; period_interval = 1 },
    @{ name = "Vacuum"; period_type = "daily"; period_interval = 2 },
    @{ name = "Clean Upstairs Bathroom"; period_type = "weekly"; period_interval = 1 },
    @{ name = "Clean Living Room Bathroom"; period_type = "weekly"; period_interval = 1 },
    @{ name = "Clean Downstairs Bathroom"; period_type = "weekly"; period_interval = 1 },
    @{ name = "Wash Sheets"; period_type = "weekly"; period_interval = 1 },
    @{ name = "Kelly - Fold Laundry"; period_type = "weekly"; period_interval = 1 }
)

foreach ($chore in $chores) {
    Invoke-GrocyPost -EntityType "chores" -Data @{
        name = $chore.name
        period_type = $chore.period_type
        period_interval = $chore.period_interval
        track_date_only = 1
    } | Out-Null
}

Write-Host "Grocy honey-do seed complete against $BaseUrl"

