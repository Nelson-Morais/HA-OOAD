// Handles Notifications in Navbar
class NotificationHandler {
    // Constructs the Object
    constructor() {
        if(notification_handler == null)
            this.loadNotifications()
    }

    // Downloads JSON Data for Notifications
    loadNotifications() {
        $.getJSON("me/notifications/", function (notification_list) {
            if (notification_list != null) {
                notification_list.forEach((notification) => {
                    notification_handler.addNotification(
                        notification.title,
                        notification.message,
                    )
                })
            } else {
                console.log("loadNotification(): No notifications found.")
            }
        })
    }

    // Add Notifications to Notification List
    addNotification(title, text) {
        let dropdown = document.getElementById("notificationDropdown")
        if (dropdown != null) {
            // Create Notification Elements
            let notification_root = document.createElement("li")
            let notification_link = document.createElement("a")
            notification_link.classList.add("dropdown-item")
            notification_link.classList.add("notification")
            let notification_title = document.createElement("strong")
            let notification_br = document.createElement("br")

            // Fill Elements with Text
            notification_title.innerText = title
            let notification_text = text

            // Stick Notification Elements together
            notification_root.append(notification_link)
            notification_link.append(notification_title, notification_br, notification_text)

            // Add to Dropdown List
            dropdown.append(notification_root)
        } else {
            console.log("updateNotification(): No Dropdown found.")
        }
    }
}

// Run initial Setup
var notification_handler = new NotificationHandler()
