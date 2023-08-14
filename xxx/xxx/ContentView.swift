//
//  ContentView.swift
//  xxx
//
//  Created by 권태웅 on 2023/07/28.
//

import SwiftUI

struct ContentView: View {
    @Binding var document: xxxDocument

    var body: some View {
        TextEditor(text: $document.text)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(document: .constant(xxxDocument()))
    }
}
