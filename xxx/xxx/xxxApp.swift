//
//  xxxApp.swift
//  xxx
//
//  Created by 권태웅 on 2023/07/28.
//

import SwiftUI

@main
struct xxxApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: xxxDocument()) { file in
            ContentView(document: file.$document)
        }
    }
}
