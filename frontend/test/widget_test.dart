// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:frontend/main.dart';

void main() {
  testWidgets('CulinaryLens app smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const CulinaryLensApp());

    // Verify that our app loads correctly.
    expect(find.text('CulinaryLens'), findsOneWidget);
    expect(find.text('Welcome to CulinaryLens'), findsOneWidget);
    expect(find.byIcon(Icons.camera_alt), findsAtLeastNWidgets(1));
  });
}
