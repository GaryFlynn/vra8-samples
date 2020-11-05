function handler($context, $payload) {
  Write-Host "Hello " $payload.target
  return $payload
}