import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter layout demo'),
        ),
        body: const Center(
          child: Column(
            children: [
              Expanded(
                  child: Row(
                    children: [
                      Text("테스트 중.."),
                      Icon(Icons.sms_failed),
                      TextField()
                    ],
                  )
              )
            ],
          )
        ),
        bottomNavigationBar: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Icon(Icons.phone),
            Icon(Icons.home),
            Icon(Icons.sms_rounded),
          ],
        ),
      ),
    );
  }
}