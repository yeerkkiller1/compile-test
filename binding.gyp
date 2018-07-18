{
  "targets": [
    {
      "target_name": "native",
      "sources": [
        "native.cpp"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}