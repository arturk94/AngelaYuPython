import QtQuick 2.15
import QtQuick.Controls 2.15
ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "HelloApp"
    property string currTime: "00:00:00"
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/playas.jpg"
            fillMode: Image.PreserveAspectCrop
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime  // used to be; text: "16:38:33"
                font.pixelSize: 48
                color: "white"
            }
        }
    }
}