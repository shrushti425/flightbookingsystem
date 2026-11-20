# SkyDesk: A Four-Stage Airline Reservation and Ticketing System

SkyDesk is an end-to-end flight reservation workflow that takes a passenger from account creation to a printed ticket. It models the booking process as four sequential stages: authentication, trip selection, payment, and ticket generation.

## Motivation

Airline booking looks simple on the surface, but it combines several core software engineering concerns: user authentication, input validation, stateful multi-step workflows, price computation with optional add-ons, and document generation. I chose this project to build a complete transactional system from scratch, where each stage depends on the correctness of the one before it.

## Problem Statement

Booking a flight typically involves several disconnected steps: creating an account, choosing a route and date, selecting optional services, calculating the final fare, and obtaining a ticket. Errors at any step, such as an invalid date or a miscalculated total, propagate to the final ticket.

SkyDesk addresses this by:

- Guiding the user through a fixed, ordered workflow so no step can be skipped
- Calculating the final fare transparently from the selected destination and add-ons
- Generating a printable ticket only after payment is confirmed

## Key Features

- **User authentication:** Sign-up and login for new and returning users
- **Destination selection:** Choose from a predefined set of destinations
- **Date selection:** Pick a travel date from the available options
- **Optional services:** Add in-flight meals to a booking
- **Fare calculation:** Itemized total covering base fare and add-ons
- **Payment confirmation:** Ticket generation is gated on completed payment
- **Ticket printing:** Final boarding pass with booking details

## System Workflow

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Authentication | The user signs up or logs in and is greeted by name |
| 2 | Trip Selection | The user selects a destination, travel date, and optional add-ons |
| 3 | Payment | The system computes the total fare and processes the payment |
| 4 | Ticket Generation | The system prints the ticket with the confirmed booking details |

## Tech Stack

- **Language:** [e.g., Python 3.x / Java / C++]
- **Interface:** [e.g., Command-line / Tkinter GUI / Web]
- **Data storage:** [e.g., CSV files / SQLite / in-memory]

## File Structure

```
skydesk/
|-- [main file]          # Entry point, controls the four-stage flow
|-- [auth module]        # Sign-up and login logic
|-- [booking module]     # Destination, date, and add-on selection
|-- [payment module]     # Fare calculation and payment handling
|-- [ticket module]      # Ticket generation and printing
|-- README.md
```

## Getting Started

### Prerequisites

- [Language and version, e.g., Python 3.10 or higher]

### Installation and Run

```bash
git clone https://github.com/[your-username]/[repo-name].git
cd [repo-name]
[run command, e.g., python main.py]
```

## Usage

1. Launch the application and choose to sign up or log in.
2. Select a destination, travel date, and any in-flight services.
3. Review the itemized fare and confirm payment.
4. Print the generated ticket.

## Design Decisions

- **Sequential stage gating:** Each stage must complete before the next begins, which prevents tickets from being issued for unpaid or incomplete bookings.
- **Separation of concerns:** Authentication, booking, payment, and ticketing are kept as distinct responsibilities, making each easier to test and extend.

## Limitations and Future Work

- Payment is simulated and does not integrate with a real payment gateway
- Destinations and dates are predefined rather than pulled from a live flight database
- Planned extensions: seat selection, booking cancellation and modification, persistent user history, and a web-based front end

## Contributing

This is an individual project. Suggestions and bug reports are welcome through GitHub Issues.

## Author

**Shrushti**
B.Tech Electronics and Communication Engineering (AI/ML specialization), MIT World Peace University, Pune
Website: shrushtiraut.com

## License

[MIT License / specify]
