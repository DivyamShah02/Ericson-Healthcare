import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';
import 'package:path_provider/path_provider.dart';
import 'package:permission_handler/permission_handler.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: WebViewScreen(),
    );
  }
}

class WebViewScreen extends StatefulWidget {
  @override
  _WebViewScreenState createState() => _WebViewScreenState();
}

class _WebViewScreenState extends State<WebViewScreen> {
  late InAppWebViewController webViewController;
  final String url = "https://ericsontpa.pythonanywhere.com/";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Flutter WebView")),
      body: InAppWebView(
        initialUrlRequest: URLRequest(url: WebUri.uri(Uri.parse(url))),
        initialSettings: InAppWebViewSettings(
          javaScriptEnabled: true,
          mediaPlaybackRequiresUserGesture: false,
        ),
        onWebViewCreated: (controller) {
          webViewController = controller;
        },
        androidOnPermissionRequest: (controller, origin, resources) async {
          return PermissionRequestResponse(
            resources: resources,
            action: PermissionRequestResponseAction.GRANT,
          );
        },
        onDownloadStartRequest: (controller, url) async {
          if (url != null) {
            await _downloadFile(url.toString());
          }
        },
      ),
    );
  }

  Future<void> _downloadFile(String url) async {
    try {
      print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
      print("Download URL: ${url.toString()}");
      // Get app-specific directory
      final directory = Platform.isAndroid
          ? await getExternalStorageDirectory() // App-specific external storage
          : await getApplicationDocumentsDirectory(); // App-specific internal storage

      if (directory != null) {
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
        print("${directory.path}/${url.split('/').last}");
        print("in if block");
        print("Download URL: ${url.toString()}");

        // Construct file path
        // final filePath = "${directory.path}/${url.split('/').last}";
        final filePath = "${directory.path}/sample.pdf";
        final file = File(filePath);

        // Start downloading the file
        final request = await HttpClient().getUrl(Uri.parse(url));
        final response = await request.close();
        await response.pipe(file.openWrite());

        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Downloaded to $filePath")),
        );
      } else {
        throw Exception("Storage directory not accessible.");
      }
    } catch (e) {
      print("in catch block");
      print("Download URL: ${url.toString()}");

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Download failed: $e")),
      );
    }
  }
}

//   Future<void> _downloadFile(String url) async {
//     if (await Permission.storage.request().isGranted) {
//       final directory = await getExternalStorageDirectory();
//       if (directory != null) {
//         final filePath = "${directory.path}/${url.split('/').last}";
//         final file = File(filePath);

//         try {
//           final request = await HttpClient().getUrl(Uri.parse(url));
//           final response = await request.close();
//           await response.pipe(file.openWrite());
//           ScaffoldMessenger.of(context).showSnackBar(
//             SnackBar(content: Text("Downloaded to $filePath")),
//           );
//         } catch (e) {
//           ScaffoldMessenger.of(context).showSnackBar(
//             SnackBar(content: Text("Download failed: $e")),
//           );
//         }
//       }
//     } else {
//       ScaffoldMessenger.of(context).showSnackBar(
//         SnackBar(content: Text("Storage permission denied")),
//       );
//     }
//   }
// }
