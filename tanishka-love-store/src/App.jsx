import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Heart, ShoppingCart, Mail, Star, Sparkles, Moon, MessageCircle, Gift } from 'lucide-react'
import './App.css'

function App() {
  const [cart, setCart] = useState([])
  const [showCart, setShowCart] = useState(false)

  const products = [
    {
      id: 1,
      name: "Unlimited Hugs",
      price: "₹0",
      description: "Warm, cozy hugs whenever you need them. Unlimited stock available!",
      icon: "🤗",
      delivery: "Instant delivery",
      stock: "Unlimited",
      category: "Physical Affection"
    },
    {
      id: 2,
      name: "Premium Cuddles",
      price: "Free",
      description: "Soft, comfortable cuddles with 1-click delivery. Perfect for movie nights!",
      icon: "🥰",
      delivery: "1 click delivery",
      stock: "Always Available",
      category: "Physical Affection"
    },
    {
      id: 3,
      name: "Late-Night Talks",
      price: "Priceless",
      description: "Deep conversations under the stars. Share your dreams and thoughts.",
      icon: "🌙",
      delivery: "Add to cart",
      stock: "Endless",
      category: "Emotional Connection"
    },
    {
      id: 4,
      name: "Sweet Kisses",
      price: "Free",
      description: "Gentle, loving kisses that make your heart flutter.",
      icon: "💋",
      delivery: "On demand",
      stock: "Infinite",
      category: "Physical Affection"
    },
    {
      id: 5,
      name: "Morning Texts",
      price: "₹0",
      description: "Good morning messages to start your day with a smile.",
      icon: "☀️",
      delivery: "Daily delivery",
      stock: "365 days",
      category: "Communication"
    },
    {
      id: 6,
      name: "Surprise Dates",
      price: "Love",
      description: "Spontaneous romantic dates planned just for you.",
      icon: "🎁",
      delivery: "Surprise timing",
      stock: "Monthly",
      category: "Experiences"
    },
    {
      id: 7,
      name: "U know what i mean hehe ",
      price: "10rs",
      description: "I don't disappoint.",
      icon: "👂",
      delivery: "24/7 available",
      stock: "Always",
      category: "Physical Affection"
    },
    {
      id: 8,
      name: "Silly Jokes",
      price: "Laughter",
      description: "Funny jokes and puns to make you giggle all day.",
      icon: "😄",
      delivery: "Random delivery",
      stock: "Unlimited",
      category: "Entertainment"
    }
  ]

  const addToCart = (product) => {
    setCart([...cart, { ...product, id: Date.now() }])
  }

  const removeFromCart = (id) => {
    setCart(cart.filter(item => item.id !== id))
  }

  const sendOrder = async () => {
    if (cart.length === 0) {
      alert("Your cart is empty! Add some love first 💕")
      return
    }

    try {
      // Prepare cart items for backend
      const cartItems = cart.map(item => ({
        name: item.name,
        price: item.price,
        delivery: item.delivery,
        icon: item.icon,
        category: item.category
      }))

      // Send order to backend
      const response = await fetch('/api/send-order', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          cart_items: cartItems
        })
      })

      const result = await response.json()

      if (response.ok) {
        alert(`Order sent successfully! 💕\n\nSent ${result.order_details.total_items} items to ${result.order_details.sent_to}`)
        setCart([])
        setShowCart(false)
      } else {
        alert(`Failed to send order: ${result.error}`)
      }
    } catch (error) {
      console.error('Error sending order:', error)
      alert('Failed to send order. Please try again later.')
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 via-rose-50 to-pink-100">
      {/* Header */}
      <header className="bg-gradient-to-r from-pink-200 to-rose-200 shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <Heart className="h-8 w-8 text-pink-600 animate-pulse" />
              <div>
                <h1 className="text-3xl font-bold text-pink-800">Tanishka's Love Store</h1>
                <p className="text-pink-600">From Manas with Love 💕</p>
              </div>
            </div>
            <Button 
              onClick={() => setShowCart(!showCart)}
              className="bg-pink-500 hover:bg-pink-600 text-white relative"
            >
              <ShoppingCart className="h-5 w-5 mr-2" />
              Cart ({cart.length})
              {cart.length > 0 && (
                <Badge className="absolute -top-2 -right-2 bg-red-500 text-white">
                  {cart.length}
                </Badge>
              )}
            </Button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-12 text-center">
        <div className="container mx-auto px-4">
          <h2 className="text-5xl font-bold text-pink-800 mb-4">
            Welcome to Your Personal Love Store! 💖
          </h2>
          <p className="text-xl text-pink-600 mb-8">
            Everything you need for unlimited love and happiness, specially curated by Manas
          </p>
          <div className="flex justify-center space-x-4 text-pink-500">
            <Sparkles className="h-8 w-8 animate-bounce" />
            <Heart className="h-8 w-8 animate-pulse" />
            <Sparkles className="h-8 w-8 animate-bounce" />
          </div>
        </div>
      </section>

      <div className="container mx-auto px-4 pb-12">
        <div className="flex flex-col lg:flex-row gap-8">
          {/* Products Grid */}
          <div className="flex-1">
            <h3 className="text-2xl font-bold text-pink-800 mb-6 text-center">
              💕 Love Products Collection 💕
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {products.map((product) => (
                <Card key={product.id} className="bg-white/80 backdrop-blur-sm border-pink-200 hover:shadow-xl transition-all duration-300 hover:scale-105">
                  <CardHeader className="text-center">
                    <div className="text-4xl mb-2">{product.icon}</div>
                    <CardTitle className="text-pink-800">{product.name}</CardTitle>
                    <CardDescription className="text-pink-600">
                      {product.description}
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="text-center">
                    <div className="space-y-2">
                      <div className="text-2xl font-bold text-pink-700">{product.price}</div>
                      <Badge variant="secondary" className="bg-pink-100 text-pink-700">
                        {product.delivery}
                      </Badge>
                      <div className="text-sm text-pink-500">
                        Stock: {product.stock}
                      </div>
                      <Badge variant="outline" className="border-pink-300 text-pink-600">
                        {product.category}
                      </Badge>
                    </div>
                  </CardContent>
                  <CardFooter>
                    <Button 
                      onClick={() => addToCart(product)}
                      className="w-full bg-gradient-to-r from-pink-400 to-rose-400 hover:from-pink-500 hover:to-rose-500 text-white"
                    >
                      <Heart className="h-4 w-4 mr-2" />
                      Add to Cart
                    </Button>
                  </CardFooter>
                </Card>
              ))}
            </div>
          </div>

          {/* Cart Sidebar */}
          {showCart && (
            <div className="lg:w-80">
              <Card className="bg-white/90 backdrop-blur-sm border-pink-200 sticky top-4">
                <CardHeader>
                  <CardTitle className="text-pink-800 flex items-center">
                    <ShoppingCart className="h-5 w-5 mr-2" />
                    Your Love Cart
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  {cart.length === 0 ? (
                    <p className="text-pink-600 text-center py-4">
                      Your cart is empty. Add some love! 💕
                    </p>
                  ) : (
                    <div className="space-y-3">
                      {cart.map((item) => (
                        <div key={item.id} className="flex items-center justify-between p-3 bg-pink-50 rounded-lg">
                          <div className="flex items-center space-x-2">
                            <span className="text-xl">{item.icon}</span>
                            <div>
                              <div className="font-medium text-pink-800">{item.name}</div>
                              <div className="text-sm text-pink-600">{item.price}</div>
                            </div>
                          </div>
                          <Button
                            size="sm"
                            variant="outline"
                            onClick={() => removeFromCart(item.id)}
                            className="text-pink-600 border-pink-300 hover:bg-pink-100"
                          >
                            Remove
                          </Button>
                        </div>
                      ))}
                    </div>
                  )}
                </CardContent>
                {cart.length > 0 && (
                  <CardFooter>
                    <Button 
                      onClick={sendOrder}
                      className="w-full bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white"
                    >
                      <Mail className="h-4 w-4 mr-2" />
                      Send Order to Manas 💕
                    </Button>
                  </CardFooter>
                )}
              </Card>
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-gradient-to-r from-pink-200 to-rose-200 py-8 mt-12">
        <div className="container mx-auto px-4 text-center">
          <div className="flex justify-center items-center space-x-2 mb-4">
            <Heart className="h-6 w-6 text-pink-600" />
            <span className="text-pink-800 font-semibold">Made with Love by Manas for Tanishka</span>
            <Heart className="h-6 w-6 text-pink-600" />
          </div>
          <p className="text-pink-600">
            All orders will be delivered with extra love and care 💕
          </p>
          <p className="text-sm text-pink-500 mt-2">
            Orders sent to: manasxlevi@gmail.com
          </p>
        </div>
      </footer>
    </div>
  )
}

export default App

